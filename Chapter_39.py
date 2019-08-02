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
