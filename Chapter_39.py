##################################################
# Мой декоратор (не из главы 39) классов, который во время декорирования принимает от пользователя из stdin
# имена атрибутов, разделенных запятыми, и занчения атрибутов, разделенных запятыми.
# Имена атрибутов 'очищаются' от всех пробелов, значения очищаются от разделителей по краям.
# Функция required - это лишь флаг, который говорит нам запускать или нет всю перечисленную 
# выше процедуру. В итоге мы получаем первоначальный класс, дополненный атрибутами.
required = lambda: True
def extras(aClass):
    if required():
        names = input('Input attribute names separated by commas:\n')
        names = names.replace(' ','').split(',')
        values = input('Input attribute values separated by commas:\n')
        values = values.split(',')
        for i, j in enumerate(values):
            values[i] = j.strip()
            if values[i].isdigit():
                values[i] = int(j)
        aClass.gotten_attrs = {}
        for attr, value in zip(names, values):  # zip (in Python 3.x) will match exact number of 
            setattr(aClass, attr, value)        # attributes names for values. Example:
            aClass.gotten_attrs[attr] = value   # zip(['A', 'B'], [0, 1, 2]) --> (('A', 0), ('B', 1))
        return aClass                           


@extras
class Client1: pass             # Client1 = extras(Client1)

A, B,    C, D, E
1000, afdhkldfh, 1.0987,SPAM!, 103920349

Client1.gotten_attrs
X = Client1()


##################################################
class Meta(type):
    def __new__(meta, classname, supers, classdict):
        # Called by inherited method type.__call__
        print('CREATE NEW CLASS:', (meta, classname, supers, classdict), sep='\n')
        return type.__new__(meta, classname, supers, classdict)

class A(metaclass=Meta):
	def spam(self):
		pass
	attr = 'SPAM'
	num = 1000

class B(A): pass


##################################################
class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

class Eggs: 
    pass

print('making class')
class Spam(Eggs, metaclass=MetaOne):   # Inherit Eggs, is instnace of MetaOne
    data = 1
    def meth(self, arg):
        pass

print('making instnace')
X = Spam()
print('data:', X.data)


##################################################
class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.__new__:', meta, classname, supers, classdict, sep='\n   ')
        return type.__new__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):
        print('In MetaOne.__init__:', Class, classname, supers, classdict, sep='\n   ')
        print('...init class object:', list(Class.__dict__.keys()))

class Eggs:
    pass

print('making class:\n')
class Spam(Eggs, metaclass=MetaOne):   # Inherit Eggs, is instnace of MetaOne
    data = 1
    def meth(self, arg):
        pass

print('making instnace:\n')
X = Spam()
print('data:', X.data)


##################################################
# Простая функция также может играть роль метакласса

def MetaFunc(classname, supers, classdict):
    print('In MetaFunc:', classname, supers, classdict, sep='\n   ')
    return type(classname, supers, classdict)              # Return the result of type.__call__ !!!

class Eggs:
    pass

print('making class:\n')
class Spam(Eggs, metaclass=MetaFunc):   
    data = 1
    def meth(self, arg):
        pass

print('making instnace:\n')
X = Spam()
print('data:', X.data)


##################################################
# Метод __call__ можно переопределить,
# а метаклассы могут иметь свои метаклассы

print('\n' * 10)
class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.__call__: ', meta, classname, supers, classdict, sep='\n   ')
        return type.__call__(meta, classname, supers, classdict)

class SubMeta(type, metaclass=SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.__new__:', meta, classname, supers, classdict, sep='\n   ')
        return type.__new__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):
        print('In SubMeta.__init__:', Class, classname, supers, classdict, sep='\n   ')
        return type.__init__(Class, classname, supers, classdict)

class Eggs:
    pass

print('\n' * 10)
print('making class:\n'.upper())
class Spam(Eggs, metaclass=SubMeta):   
    data = 1
    def meth(self, arg):
        pass

print('\n' * 10)
print('making instnace:\n'.upper())
X = Spam()
print('data:', X.data)


##################################################
class SuperMeta:
    def __call__(self, classname, supers, classdict):
        print('In SuperMeta.__call__:', self, classname, supers, classdict, sep='\n   ')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class

class SubMeta(SuperMeta):
    def __New__(self, classname, supers, classdict):
        print('In SubMeta.__New__:', self, classname, supers, classdict, sep='\n   ')
        return type(classname, supers, classdict)
    def __Init__(self, Class, classname, supers, classdict):
        print('In SubMeta.__Init__:', self, Class, classname, supers, classdict, sep='\n   ')
        print('...init class object:', list(Class.__dict__.keys()))

class Eggs:
    pass

print('\n' * 10)
print('making class:\n'.upper())
class Spam(Eggs, metaclass=SubMeta()):       # Метакласс – экземпляр обычного класса !!!
    data = 1                                 # Вызывается в конце инструкции
    def meth(self, arg):
        pass

print('\n' * 10)
print('making instnace:\n'.upper())
X = Spam()
print('data:', X.data)


##################################################
class MetaOne(type):
    def __new__(meta, classname, supers, classdict):    # Переопределяет метод класса type
        print('In MetaOne.__new__:', meta, classname, supers, classdict, sep='\n   ')
        return type.__new__(meta, classname, supers, classdict)
    def toast(self):
        print('toast')

class Super(metaclass=MetaOne):  # Объявление метакласса наслед-ся подклассами
    def spam(self):              # MetaOne вызывается дважды при создании двух классов
        print('spam')

class C(Super):                  # Суперкласс: наследование – не экземпляр
    def eggs(self):              # Классы наследуют атрибуты суперклассов
        print('eggs')            # Но не наследуют атрибуты метаклассов

X = C()
X.eggs()               # Наследует от класса C
X.spam()               # Наследует от класса Super
X.toast()              # Не наследует от метакласса


##################################################
# Расширение вручную – добавление новых методов в классы

class Client1:
    def __init__(self, value):
        self.value = value
    def spam(self):
        return self.value * 2

class Client2:
    value = 'ni?'

def eggsfunc(obj):
    return obj.value * 4

def hamfunc(obj, value):
    return value + 'ham'

Client1.eggs = eggsfunc
Client1.ham = hamfunc

Client2.eggs = eggsfunc
Client2.ham = hamfunc

X = Client1('Ni!')
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))


##################################################
#Расширение с помощью метакласса – лучше поддерживает изменения в будущем
def eggsfunc(obj):
    return obj.value * 4

def hamfunc(obj, value):
    return value + 'ham'

class Extender(type):
    def __new__(meta, classname, supers, classdict):
        classdict['eggs'] = eggsfunc
        classdict['ham'] = hamfunc
        return type.__new__(meta, classname, supers, classdict)

class Client1(metaclass=Extender):
    def __init__(self, value):
        self.value = value
    def spam(self):
        return self.value * 2

class Client2(metaclass=Extender):
    value = 'ni?'

X = Client1('Ni!')
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))


##################################################
# Класс может формироваться, исходя из некоторых условий во время выполнения

class MetaExtend(type):
    def __new__(meta, classname, supers, classdict):
        if sometest():
            classdict['eggs'] = eggsfunc1
        else:
            classdict['eggs'] = eggsfunc2
        if someothertest():
            classdict['ham'] = hamfunc
        else:
            classdict['ham'] = lambda *args: 'Not supported'
        return type.__new__(meta, classname, supers, classdict)


##################################################
# Расширение с помощью декоратора: реализует те же действия, что и метод
# __init__ метакласса

def eggsfunc(obj):
    return obj.value * 4

def hamfunc(obj, value):
    return value + 'ham'

def Extender(aClass):
    aClass.eggs = eggsfunc              # Управляет классом, а не экземпляром
    aClass.ham = hamfunc    # Аналог метода __init__ метакласса
    return aClass

@Extender
class Client1:                        # Client1 = Extender(Client1)
    def __init__(self, value):        # Повторно присваивает оригинальному имени
        self.value = value            # класса значение функции-декоратора
    def spam(self):                   # в конце инструкции class
        return self.value * 2

@Extender
class Client2:
    value = 'ni?'

X = Client1('Ni!')             # X – экземпляр класса Client1
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))


##################################################
