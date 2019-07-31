##################################################
def decorator(F):
    print('Called decorator, get function:', F)
    F.data = 1000
    return F

@decorator
def func(x, y):
    return x + y


##################################################
def decorator(F):
    print('Called decorator, get function:', F)
    def wrapper(*args):
        print('I got arguments:', *args)
        F(*args)
    return wrapper

@decorator
def func(x, y):     # func = decorator(func) --> func = decorator.<locals>.funcX
    print(x + y)


##################################################
class decorator:
    def __init__(self, func):
        print('Called decorator, get function:', func)
        self.func = func
    def __call__(self, *args):
        print('I got arguments:', *args)
        self.func(*args)

@decorator        
def func(x, y):     # func = decorator(func) - instance of class 'decorator'
    print(x + y)    
# "Called decorator, get function: <function func at 0x7f3692ed7f28>"
# func.func - <function func at 0x7f3692ed7f28>


##################################################               
def decorator(F):
    print('Called decorator, get function:', F)
    def wrapper(*args):
        print('I got arguments:', *args)
        F(*args)
    return wrapper

@decorator        
def func(x, y):     
    print(x + y) 

class C:
    @decorator
    def method(self, x, y):  # C.method = decorator(C.method); 
        print(x * y)         # 'decorator' - simple function, not an instance of a class!!!


##################################################
def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)
        def __getattr__(self, name):
            print("Wrapper.__getattr__ '{0}' ---> {1}.__getattr__ '{0}'".format(name, self.wrapped.__class__.__name__))
            return getattr(self.wrapped, name)
    return Wrapper

@decorator
class C:                        # C = decorator(C)
    def __init__(self, x, y):   # called by Wrapper.__init__
        self.attr = 'spam: ' + str(x) + str(y)

x = C(100, 500)
print(x.attr)

@decorator
class A:
    def __init__(self, *args):
        self.args = args

y = A(100, 200, 300, 'a')
print(y.args)


##################################################
class Decorator:
    def __init__(self, C):    # During decoration @: C = Decorator(C)
        self.C = C            # Save an original class, not an instance!
    def __call__(self, *args):  # During an instance creation: C(*args) (---> Decorator(C)(*rags))
        self.wrapped = self.C(*args)  # Save an instance of an original class in the attribute 'wrapped'
        return self
    def __getattr__(self, attrname):
        return getattr(self.wrapped, attrname)  # References to the wrapped instance

@Decorator
class C:                        # C = Decorator(C) => C is an instnace fo class Decorator !!! 
    def __init__(self, x, y):   # called by Decorator.__call__(C, x, y)
        self.attr = (x, y)

x = C()
y = C()         # Will override 'x'!


##################################################
def decorator(C):                 # During decoration @: C = Decorator(C)
    class Wrapper:
        def __init__(self, *args):  # During an instance creation
            self.wrapped = C(*args)
    return Wrapper

@decorator
class B:                        
    def __init__(self, x, y):   
        self.attr = (x, y)

# Other case:
class Wrapper:
    def __init__(self, instance): 
        self.wrapped = instance   # Wrapper().wrapped = C(*args)

def decorator(C):                 # During decoration @: C = Decorator(C)
    def onCall(*args):            # During an instance creation
        return Wrapper(C(*args))  # Embeds an instance into an instance
    return onCall

@decorator
class C:                        # C = Decorator(C) => C is an instnace fo class Decorator !!! 
    def __init__(self, x, y):   # called by Decorator.__call__(C, x, y)
        self.attr = (x, y)

# Check: 
x = B(10, 20); X = C(10, 20)
y = B(30, 40); Y = C(30, 40)
for i in (x, y, X, Y):
    print(i.wrapped.attr)


##################################################
def d1(F): return F

def d2(F): return F

def d3(F): return F

@d1
@d2
@d3
def func():
    print('spam')

func()


##################################################
def d1(F):
    print('decorator d1')
    return lambda: 'X' + F()

def d2(F):
    print('decorator d2')
    return lambda: 'Y' + F()

def d3(F):
    print('decorator d3')
    return lambda: 'Z' + F()

@d1
@d2
@d3
def func():          # func = d1(d2(d3(func)))
    return 'spam'

print(func())


##################################################
# file: filler.py

def filler(collection={}):
    '''
    This function will help you to create and quickly fill a dictionary.
    If you pass in argument your existing dictionary the function will 
	fill it with a copy.
	'''
    collection = collection.copy()
    print('Press Ctrl+C to stop filling')
    try:
        while True:
            attr_value = input('ATTR=VALUE: ')
            attr_value = attr_value.replace(' ', '').split('=')
            collection[attr_value[0]] = attr_value[1]
    except KeyboardInterrupt:
        print('...\nThe end')
    return collection


##################################################
class tracer:
    def __init__(self, func):   # at the stage of decoration @:
        self.calls = 0          # saves orginal function 'func'
        self.func = func
    def __call__(self, *args):  # On subsequent calls:
        self.calls += 1         # calls the oroginal function 'func'
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)

@tracer
def spam(a, b, c):    # spam = tracer(spam) - 'spam' is an instance of the class 'tracer' 
    print(a + b + c)  # Wraps the spam function with a decorator object

# Equivalent implementation without the use of a decorator:
calls = 0
def tracer(func, *args):
    global calls
    calls += 1
    print('call %s to %s' % (calls, func.__name__))
    func(*args)

def spam(a, b, c):
    print(a, b, c)


##################################################
class tracer:                   # The state saves in attributes of an instance
    def __init__(self, func):   # At the stage of decoration @:
        self.calls = 0          # Saves orginal function 'func'
        self.func = func
    def __call__(self, *args, **kwargs):  # Called when accessed to the oroginal function 'func'
        self.calls += 1 
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args, **kwargs)

@tracer
def spam(a, b, c):    # spam = tracer(spam)
    print(a + b + c)  # calls method tracer.__init__

@tracer
def eggs(x, y):
    print(x ** y)

spam(1, 2, 3)        # tracer.__call__
spam(a=1, b=2, c=3)  # spam - an attribute of the instance

eggs(2, 16)          # self.func = eggs
eggs(4, y=4)


##################################################
calls = 0
def tracer(func):
    def wrapper(*args, **kwargs):
        global calls       # 'calls' is a global variable that is 
        calls += 1         # common to all functions, not to each function individually
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper

@tracer
def spam(a, b, c):    # spam = tracer(spam)
    print(a + b + c)  

@tracer
def eggs(x, y):
    print(x ** y)

spam(1, 2, 3)        
spam(a=1, b=2, c=3)  

eggs(2, 16)          
eggs(4, y=4)


##################################################
# file: calc.py

def calc():
    hint = '''
'?' - help
'*' - multiplication. Ex.: x * y
'/' - division. Ex.: x / y
'+' - addition. Ex.: x + y
'-' - subtraction. Ex.: x - y
'**' - exponentiation. Ex.: x ** y
'()' - prioritization. Ex.: (x + y) * z
'%' - remainder of division. Ex.: x % y
'//' - obtaining the integer part of the division. Ex.: x // y
'abs()' - number modulus. Ex.: abs(x)
'-x' - the change of the sign of the number. Ex.: -x
'divmod(x, y)' - a couple (x // y, x % y). Ex.: divmod(x, y)
'pow(x, y[,z])' - x^y modulo (if the module is specified). Ex.: pow(x, y, z)
'''
    while True:
        try:
            x = input("Expression or '?' for help: ")
            if '?' in x:    # Calls help hint
                print(hint)
                continue
            else:
                res = eval(x)   # Dangerous operation!!!
        except SyntaxError as E:    # Errors of an input
            print('SyntaxError:', E)
            continue
        if type(res) not in [float, int, complex]:   # check the type
            print('TypeError:', res)
            continue
        else:
            print(res)


##################################################
def tracer(func):
    calls = 0
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper

@tracer
def spam(a, b, c):    # spam = tracer(spam)
    print(a + b + c)  

@tracer
def eggs(x, y):
    print(x ** y)

spam(1, 2, 3)        
spam(a=1, b=2, c=3)  

eggs(2, 16)          
eggs(4, y=4)


##################################################
def tracer(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print('call %s to %s' % (wrapper.calls, func.__name__))
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


##################################################
class tracer:                   
    def __init__(self, func):   
        self.calls = 0          
        self.func = func
    def __call__(self, *args, **kwargs):  
        self.calls += 1 
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

@tracer
def spam(a, b, c):
    print(a + b + c)

spam(1, 2, 3)
spam(a=1, b=2, c=3)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    @tracer
    def giveRaise(self, percent):  # giveRaise = tracer(giverRaise)
        self.pay *= (1.0 + percent)
    @tracer
    def lastName(self):            # lastName = tracer(lastName)
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)   
bob.giveRaise(.25)                 # ERROR!
print(bob.lastName())              # ERROR!


##################################################
def tracer(func):
    calls = 0
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))	
        return func(*args, **kwargs)
    return onCall

@tracer
def spam(a, b, c):      # spam = tarcer(spam)
    print(a + b + c)    # onCall will save link on 'spam'

spam(1, 2, 3)
spam(a=4, b=5, c=6)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    @tracer
    def giveRaise(self, percent):  # giveRaise = tracer(giverRaise)
        self.pay *= (1.0 + percent)
    @tracer
    def lastName(self):            # lastName = tracer(lastName)
        return self.name.split()[-1]

print('methods...')
bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)              
sue.giveRaise(.10)
print(sue.pay)
print(bob.lastName(), sue.lastName())


##################################################
class Descriptor:
    def __get__(self, instance, owner):
        print(self, instance, owner, end='\n')
        return instance.__dict__

class Subject:  
    def __init__(self, name):
        self._name = name
    attr = Descriptor()

X = Subject('ATTRIBUTE')
X.attr


##################################################
class tracer(object):                  # Page 1110
    def __init__(self, func):                            # На этапе декорирования @
        print("[TEST] tracer.__init__:", self, func)
        self.calls = 0
        self.func = func  # Сохраняет функцию для последующего вызова
    def __call__(self, *args, **kwargs):  # Вызывается при обращениях к оригинальной функции
        self.calls += 1
        print("[TEST] tracer.__call__:", *args, **kwargs)
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)        
    def __get__(self, instance, owner):     # Вызывается при обращении к атрибуту
        return wrapper(self, instance)   # ?????????????????

class wrapper:
    def __init__(self, desc, subj):            # Сохраняет оба экземпляра 
        print("[TEST] wrapper.__init__:", self, desc, subj)
        self.desc = desc      # Делегирует вызов дескриптору
        self.subj = subj
    def __call__(self, *args, **kwargs):
        print("[TEST] wrapper.__call__:", self, *args, **kwargs)
        return self.desc(self.subj, *args, **kwargs)     # Вызовет tracer.__call__

@tracer
def spam(a, b, c):      # spam = tarcer(spam)
    print(a + b + c)    # использует только __call__

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    @tracer
    def giveRaise(self, percent):  # giveRaise = tracer(giverRaise)
        self.pay *= (1.0 + percent)
    @tracer
    def lastName(self):            # lastName = tracer(lastName)
        return self.name.split()[-1]


##################################################
class tracer:
    def __init__(self, func):
        print("[TEST] tracer.__init__:", self, func)
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        print("[TEST] tracer.__call__:", self, args, kwargs)
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):    # Вызывается при обращении к методу
        print("[TEST] tracer.__get__:", instance, owner)
        def wrapper(*args, **kwargs):      # Сохраняет оба экземпляра 
            print("[TEST] tracer.__get__.wrapper:", args, kwargs)
            return self(instance, *args, **kwargs)   # Вызовет __call__ 		
        return wrapper

spam(1, 2, 3)
spam(a=4, b=5, c=6)

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)              
bob.giveRaise(.20)
sue.giveRaise(.10)
print(bob.pay, sue.pay)
print(bob.lastName(), sue.lastName())


##################################################
# file: timer_decor.py

import time

class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        elapsed = time.time() - start
        self.alltime += elapsed
#        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        print('{0}: {1:.5f}, {2:.5f}'.format(self.func.__name__, elapsed, self.alltime))
        return result

@timer
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))

result = listcomp(5)
a = listcomp(50000)           # Use assignment to avoid output to stdout
b = listcomp(500000)
c = listcomp(1000000)
print(result)
print('allTime = {0}'.format(listcomp.alltime))

print('')
result = mapcall(5)
a = mapcall(50000)            # Use assignment to avoid output to stdout
b = mapcall(500000)
c = mapcall(1000000)
print(result)
print('allTime = {0}'.format(mapcall.alltime))

print('')
print('map/comp = {0}'.format(round(mapcall.alltime / listcomp.alltime, 5)))


##################################################
# file: mytools.py

import time

def timer(label='', trace=True):    # Arguments of the decorator saves
    class Timer:                    # class Timer is the actual decorator 
        def __init__(self, func):   # At the stage of decoration, 
            self.func = func        # the decorated function is preserved
            self.alltime = 0
        def __call__(self, *args, **kwargs):  # When called: the original is called    
            start = time.time()
            result = self.func(*args, **kwargs)
            elapsed = time.time() - start
            self.alltime += elapsed
            if trace:
                format = '{0} {1}: {2:.5f}, {3:.5f}'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format.format(*values))
            return result
    return Timer

@timer('==>')                         # listcomp = timer('==>')(listcomp)
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer('==>')
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))


##################################################
# file: testseqs.py

from mytools import timer

@timer(label='[CCC]==>')
def listcomp(N):                      # То же, что и listcomp = timer(...)(listcomp)
    return [x * 2 for x in range(N)]       # listcomp(...) вызовет Timer.__call__

@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))

for func in (listcomp, mapcall):
    print('')
    result = func(5)      # Хронометраж вызова, всех вызовов, возвращаемое значение
    func(50000)
    func(500000)
    func(1000000)
    print(result)
    print('allTime = %s' % func.alltime) # Общее время всех вызовов

print('map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))


##################################################
instances = {}
def getInstance(aClass, *args, **kwargs):     # Manages the global table
    if aClass not in instances:
        instances[aClass] = aClass(*args, **kwargs)   # One dictionary element per class
    return instances[aClass]

def singleton(aClass):
    def onCall(*args, **kwargs):
        return getInstance(aClass, *args, **kwargs)
    return onCall


@singleton                                     # Person = singleton(Person)
class Person:                                  # Assigns onCall to the Person name
    def __init__(self, name, hours, rate):     # onCall will save Person
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate

@singleton
class Spam:
    def __init__(self, val):
        self.attr = val

bob = Person('Bob', 40, 10)    
print(bob.name, bob.pay())

sue = Person('Sue', 50, 20)
print(sue.name, sue.pay())

X = Spam(42)
Y = Spam(99)
print(X.attr, Y.attr)


##################################################
def singleton(aClass):                  # At the stage of decoration @:
    instance = None
    def onCall(*args, **kwargs):        # At the stage of creation of an instance 
        nonlocal instance               # nonlocal - from Python 3.0 and upper
        if instance == None:
            instance = aClass(*args, **kwargs)  # At the same scope on each class
        return instance
    return onCall

-- // --


##################################################
class singleton:
    def __init__(self, aClass):        # At the stage of decoration @:
        self.aClass = aClass
        self.instance = None
    def __call__(self, *args, **kwargs):    # At the stage of creation of an instance 
        if self.instance == None:
            self.instance = self.aClass(*args, **kwargs)      # One instance per class
        return self.instance

-- // --


##################################################
class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapped, attrname)

x = Wrapper([1, 2, 3])
x.append(4)
x.wrapped
x = Wrapper({'a': 1, 'b': 2})
list(x.keys())


##################################################
# file: tracer.py

def Tracer(aClass):                         # At the stage of decoration @:
    class Wrapper:
        def __init__(self, *args, **kwargs):        # At the stage of creation of an instance
            self.fetches = 0
            self.wrapped = aClass(*args, **kwargs)
        def __getattr__(self, attrname):
            print('Trace: ' + attrname)
            self.fetches += 1
            return getattr(self.wrapped, attrname)
    return Wrapper


@Tracer
class Spam:                            # Spam = Tracer(Spam)
    def display(self):
        print('Spam!' * 8)

@Tracer
class Person:                                  
    def __init__(self, name, hours, rate):     
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate


food = Spam()
food.display()             # __getattr__
print([food.fetches])      # Inner call - Wrapper will not use        

bob = Person('Bob', 40, 50)    # bob - instanceof class Wrapper !!!
print(bob.name)
print(bob.pay())

sue = Person('Sue', rate=100, hours=60)
print(sue.name)
print(sue.pay())

print(bob.name)
print(bob.pay())
print([bob.fetches, sue.fetches])


##################################################
from tracer import Tracer        # In module tracer.py
@Tracer
class MyList(list): pass         # MyList = Tracer(MyList)

x = MyList([1, 2, 3])            # will call Wrapper()
x.append(4)                      # will call __getattr__, append
x.wrapped
WrapList = Tracer(list)          # Handmade decoration
x = WrapList([4, 5, 6])
x.append(7)
x.wrapped


##################################################
class Tracer:
    def __init__(self, aClass):      # At the stage of decoration @
        self.aClass = aClass         # Uses attributes of an instance
    def __call__(self, *args, **kwargs):       # At the stage of an instance creation
        self.wrapped = self.aClass(*args, **kwargs)     # THE ONLY ONE (RECENT) INSTANCE FOR EACH CLASS!
        return self
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)

@Tracer                             # will call __init__
class Spam:                         # Spam = Tracer(Spam)     # Spam is <__main__.Tracer object at ...>
    def display(self, N=10):
        print('Spam!' * N)
    def printer(self):
        print(self, Spam.wrapped)
    
(food, X, Z) = (Spam(), Spam(), Spam())      # will call __call__
for i in (food, X, Z):
#    i.display()           # will call __getattr__
    i.printer()           # will call __getattr__
     

@Tracer                             # will call __init__
class Person:                       # Person = Tracer(Person)
    def __init__(self, name): 
        self.name = name

bob = Person('Bob')         # bob - instance of class Tracer
print(bob.name)        # The instance of class Tracer contains the instance of class Person
sue = Person('Sue')
print(sue.name)        # Instance use rewrite instance bob
print(bob.name)        # Ooops... now Bob's name is 'Sue' =(


##################################################
instances = {}
def getInstance(aClass, *args):
    if aClass not in instances:
        instances[aClass] = aClass(*args)
    return instances[aClass]

bob = getInstance(Person, 'Bob', 40, 10) # Вместо: bob = Person('Bob', 40, 10)


##################################################
instances = {}
def getInstance(object):
    aClass = object.__class__
    if aClass not in instances:
        instances[aClass] = object
    return instances[aClass]

bob = getInstance(Person('Bob', 40, 10)) # Вместо: bob = Person('Bob', 40, 10)


##################################################
# Registration of decorated objects
registry = {}
def register(obj):                 # The decorator of functions and classes
    registry[obj.__name__] = obj   # Add to the registry
    return obj                     # Return obj, but not wrapper

@register
def spam(x):                       # spam = register(spam)
    return(x ** 2)

@register                             
def ham(x):                        
    return(x ** 3)

@register
class Eggs:                        # Eggs = register(Eggs)
    def __init__(self, x):
        self.data = x ** 4
    def __str__(self):
        return str(self.data)

print('Registry:')
for name in registry:
    print(name, '=>', registry[name], type(registry[name]))

print('\nManual calls:')
print(spam(2))
print(ham(2))
X = Eggs(2)
print(X)

print('\nRegistry calls:')
for name in registry:
    print(name, '=>', registry[name](3))        # Registry call


##################################################
# Direct extension of the decorated objects
def decorate(func):
    func.marked = True      # Assigns an attribute to 
    return func             # the function for later use

@decorate
def spam(a, b):
    return a + b 

spam.marked


def annotate(text):            # The same as previous but attribute value
    def decorate(func):        # is passed as argument to the decorator
        func.label = text
        return func
    return decorate

@annotate('spam data')            
def spam(a, b):                # spam = annotate('spam data')(spam)
    return a + b

spam(1, 2), spam.label


##################################################
# file: private38.py
# Реализация частных атрибутов
'''
Ограничение на чтение значений частных атрибутов экземпляров классов.
Примеры использования приводятся в программном коде самопроверки, в конце.
Декоратор действует как: Doubler = Private('data', 'size')(Doubler).
Функция Private возвращает onDecorator, onDecorator возвращает onInstance,
а в каждый экземпляр onInstance встраивается экземпляр Doubler.
'''
traceMe = False
def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')

def Private(*privates):         # privates - в объемлющей области видимости
    def onDecorator(aClass):    # aClass - в объемлющей области видимости
        class onInstance:       # Обертывает экземпляр атрибута
            def __init__(self, *args, **kwargs):
                self.wrapped = aClass(*args, **kwargs)
            def __getattr__(self, attr):       # Для собственных атрибутов getattr не вызывается 
                trace('get:', attr)          # Другие, как предполагается, принадлежат 
                if attr in privates:         # обернутому объекту
                    raise TypeError('private attrribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)       # getattr используется вместо __dict__ потому,
                              # что атрибуты могут наследоваться от класса, а не только храниться в объекте
            def __setattr__(self, attr, value):   # Доступ извне
                trace('set:', attr, value)     # Другие обрабатываются нормально
                if attr == 'wrapped':        # Разрешить доступ к своим атрибутам (wrapped)
                    self.__dict__[attr] = value         # Избежать зацикливания         
                elif attr in privates:
                    raise TypeError('private attrribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)   # Атрибуты обернутого объекта. Или можно исп. __dict__
        return onInstance
    return onDecorator

if __name__ == '__main__':
    traceMe = True
    
    @Private('data', 'size')     # Doubler = Private('data', 'size')(Doubler)
    class Doubler:
        def __init__(self, label, start):
            self.label = label    # Доступ изнутри класса
            self.data = start     # Не перехватывается: обрабатывается как обычно
        def size(self):
            return len(self.data)       # Методы выполняются без проверки, потому
        def double(self):               # что ограничение доступа не наследуется
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        def display(self):
            print('%s => %s' % (self.label, self.data))
    
    X = Doubler('X is', [1, 2, 3])
    Y = Doubler('Y is', [-10, -20, -30])
    
    # Все следующие попытки оканчиваются успехом
    
    print(X.label)                        # Доступ извне класса
    X.display(); X.double(); X.display()  # Перехватывается: проверяется, делегируется
    print(Y.label)
    Y.display(); Y.double()
    Y.label = 'Spam'
    Y.display()
    
    # Все следующие попытки терпят неудачу
    '''
    print(X.size())    # Выведет "TypeError: private attrribute fetch: size"
    print(X.data)
    X.data = [1, 1, 1]
    X.size = lambda S: 0
    print(Y.data)
    print(Y.size())
    '''

# Вывод:
[set: wrapped <__main__.Doubler object at 0x7ff6775050b8>]
[set: wrapped <__main__.Doubler object at 0x7ff6775050f0>]
[get: label]
X is
[get: display]
X is => [1, 2, 3]
[get: double]
[get: display]
X is => [2, 4, 6]
[get: label]
Y is
[get: display]
Y is => [-10, -20, -30]
[get: double]
[set: label Spam]
[get: display]
Spam => [-20, -40, -60]

##
@private38.Private('attr1', 'attr2')
class Test:
    def __init__(self, label='', start='SPAM'):
        self.label = label
        self.attr1 = start
    attr2 = 'Hello world!'

X = Test('LABEL SPAM!', 'START SPAM!')    


##################################################
#Декораторы Private и Public
# file: access.py

'''
Декораторы Private и Public для объявления частных и общедоступных атрибутов.
Управляют доступом к атрибутам, хранящимся в экземпляре или наследуемым
от классов. Декоратор Private объявляет атрибуты, которые недоступны за
пределами декорируемого класса, а декоратор Public объявляет все атрибуты,
которые, наоборот, будут доступны. Внимание: в Python 3.0 эти декораторы
оказывают воздействие только на атрибуты с обычными именами – вызовы методов
перегрузки операторов с именами вида __X__, которые неявно производятся
встроенными операциями, не перехватываются методами __getattr__ и __getattribute__
в классах нового стиля.
Добавьте здесь реализации методов вида __X__ и с их помощью делегируйте выполнение
операций встроенным объектам.
'''
traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.__wrapped = aClass(*args, **kwargs)
            def __getattr__(self, attr):
                trace('get:', attr)
                if failIf(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.__wrapped, attr)
            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.__wrapped, attr, value)
        return onInstance
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))


# Check in interactive shell:
from access import Private, Public
@Private('age')       # Person = Private('age')(Person)
class Person:         # Person = onInstance с информацией о состоянии 
    def __init__(self, name, age):
        self.name = name
        self.age = age

X = Person('Bob', 40)
X.name
X.name = 'Sue'
X.name
X.age
X.age = 1000

@Public('name')       # Person = Public('age')(Person)
class Person:         # Public = onInstance с информацией о состоянии 
    def __init__(self, name, age):
        self.name = name
        self.age = age

X = Person('Bob', 40)
X.name
X.name = 'Sue'
X.name
X.age
X.age = 1000


##################################################
traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        def getattributes(self, attr):
            trace('get:', attr)
            if failIf(attr):
                raise TypeError('private attribute fetch: ' + attr)
            else:
                return object.__getattribute__(self, attr)
        aClass.__getattribute__ = getattributes
        return aClass
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))


##################################################
# file: devtools.py

def rangetest(*argchecks):    # Проеряет позиционные аругменты на вхождение
    def onDecorator(func):    # в заданный диапазон
        if not __debug__:     # True - если "python -0 main.py args..."
            return func       # Ничего не выполняет: просто возвращает оригинальную функцию
        else:                 # Иначе на этапе отладки возвращает обертку
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = 'Argument %s not in %s..%s' % (ix, low, high)
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator


# file: devtools_test.py

from devtools import rangetest
print(__debug__)              # False, если "pyrhon -O main.py"

@rangetest((1, 0, 120))         # persinfo = rangetest(...)persinfo
def persinfo(name, age):        # Значение 1-го аругмента - age - должно быть в диапазоне 0..120
    print('%s is %s years old' % (name, age))

@rangetest([0, 1, 12], [1, 1, 31], [2, 0, 2009])
def birthday(M, D, Y):
    print('birthday = {0}/{1}/{2}'.format(M, D, Y))

class Person:
    def __init__(self, name, job, pay):
        self.job = job
        self.name = name
        self.pay = pay
    @rangetest([1, 0.0, 1.0])     # giveRaise = rangetest(...)(giveRaise)
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

# Закомментированные строки возбуждают исключение TypeError, если сценарий
# не был запущен командой 'python -O'

persinfo('Bob Smith', 45)    # В действительности вызывает onCall(...)
#persinfo('Bob Smith', 200)  # или personinfo, если был использован аргумент -О 
                             # командной строки
birthday(5, 31, 1963)
#birthday(5, 32, 1963)

sue = Person('Sue Jones', 'dev', 100000)
sue.giveRaise(0.10)         # В действительности вызывает onCall(self, 0.10)
print(sue.pay)              # или giveRaise(self, 0.10), если использован -О
sue.giveRaise(1.10)         # TypeError: Argument 1 not in 0.0..1.0
print(sue.pay)


##################################################
# file: devtools.py

'''
Файл devtools.py: декоратор функций, выполняющий проверку аргументов на
вхождение в заданный диапазон. Проверяемые аргументы передаются декоратору в
виде именованных аргументов. В фактическом вызове функции аргументы могут
передаваться как в виде позиционных, так и в виде именованных аргументов,
при этом аргументы со значениями по умолчанию могут быть опущены.
Примеры использования приводятся в файле devtools_test.py.
'''

trace = True

def rangetest(**argchecks):   # Проверяемые аргументы с диапазонами
    def onDecorator(func):    # onCall сохраняет func и argchecks
        if not __debug__:     # True - если 'python -O main.py args...'
            return func       # Обертывание только при отладке; иначе 
        else:                 # возвращается оригинальная функция
            import sys
            code = func.__code__ if sys.version_info[0] == 3 else func.func_code
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__
            
            def onCall(*pargs, **kargs):
                # Все аргументы в кортеже pargs сопоставляются с первым N
                # ожидаемыми аргументами по позиции 
                # Остальные либо находятся в словаре kargs, либо опущены, как 
                # аргументы со значениями по умолчанию
                positionals = list(allargs)
                positionals = positionals[:len(pargs)]
                
                for (argname, (low, high)) in argchecks.items():
                    # Для всех аргументов, которые должны быть проверены
                    if argname in kargs:
                        # Аргумент был передан по имени
                        if kargs[argname] < low or kargs[argname] > high:
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                        
                    elif argname in positionals:
                        # Аргумент был передан по позиции
                        position = positionals.index(argname)
                        if pargs[position] < low or pargs[position] > high:
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                        
                    else:
                        # Аргумент не был передан: предполагается, что он 
                        # имеет значение по умолчанию
                        if trace:
                            print('Argument "{0}" dafaulted'.format(argname))
                return func(*pargs, **kargs)              # ОК: вызвать оригинальную функцию
            return onCall
    return onDecorator


##################################################
# file: devtools_test.py

# Закомментированные строки возбуждают исключение TypeError, если сценарий
# не был запущен командой 'python -O'
from devtools import rangetest

# Тест вызовов функций с позиционными и именованными аргументами

@rangetest(age=(0, 120))     # persinfo = rangetest(...)(persinfo)
def persinfo(name, age):
    print('%s is %s years old' % (name, age))

@rangetest(M=(1, 12), D=(1, 31), Y=(0, 2009))
def birthday(M, D, Y):
    print('birthday = {0}/{1}/{2}'.format(M, D, Y))

persinfo('Bob', 40)
persinfo(age=40, name='Bob')
birthday(5, D=1, Y=1963)
#persinfo('Bob', 150)
#persinfo(age=150, name='Bob')
#birthday(5, D=40, Y=1963)

# Тест вызовов методов с позиционными и именованными аргументами

class Person:
    def __init__(self, name, job, pay):
        self.job = job
        self.pay = pay
                                # giveRaise = rangetest(...)(giveRaise)
    @rangetest(percent=(0.0, 1.0)) # Аргумент percent передается по имени
    def giveRaise(self, percent): # или по позиции
        self.pay = int(self.pay * (1 + percent))

bob = Person('Bob Smith', 'dev', 100000)
sue = Person('Sue Jones', 'dev', 100000)
bob.giveRaise(.10)
sue.giveRaise(percent=.20)
print(bob.pay, sue.pay)
#bob.giveRaise(1.10)
#bob.giveRaise(percent=1.20)

# Тест вызовов функций с опущенными аргументами по умолчанию

@rangetest(a=(1, 10), b=(1, 10), c=(1, 10), d=(1, 10))
def omitargs(a, b=7, c=8, d=9):
    print(a, b, c, d)

omitargs(1, 2, 3, 4)
omitargs(1, 2, 3)
omitargs(1, 2, 3, d=4)
omitargs(1, d=4)
omitargs(d=4, a=1)
omitargs(1, b=2, d=4)
omitargs(d=8, c=7, a=1)
#omitargs(1, 2, 3, 11)    # Недопустимое значение аргумента d
#omitargs(1, 2, 11)       # Недопустимое значение аргумента c
#omitargs(1, 2, 3, d=11)  # Недопустимое значение аргумента d
#omitargs(11, d=4)        # Недопустимое значение аргумента a
#omitargs(d=4, a=11)      # Недопустимое значение аргумента a
#omitargs(1, b=11, d=4)   # Недопустимое значение аргумента b
#omitargs(d=8, c=7, a=11) # Недопустимое значение аргумента a


##################################################
def func(a, b, c, d):
    x = 1
    y = 2

code = func.__code__
code
<code object func at 0x7f6f52b930c0, file "<stdin>", line 1>
code.co_nlocals
6
code.co_varnames
('a', 'b', 'c', 'd', 'x', 'y')
code.co_varnames[:code.co_argcount]
('a', 'b', 'c', 'd')
import sys
sys.version_info
sys.version_info(major=3, minor=6, micro=6, releaselevel='final', serial=0)
list(sys.version_info)
[3, 6, 6, 'final', 0]
code = func.__code__ if sys.version_info[0] == 3 else func.func_code

def func(a, b, c, d=10):
    x = 1
    y = 2


##################################################
# Tasks at the end of Chapter 38. Task 1
# file: mytools.py

import time
def timer(label='', trace=True):    # Arguments of the decorator saves
    def onDecorator(func):          # At the stage of decoration
        def onCall(*args, **kwargs):  # When called: the original is called    
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            onCall.alltime += elapsed
            if trace:
                format = '{0} {1}: {2:.5f}, {3:.5f}'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format.format(*values))
            return result
        onCall.alltime = 0            # Assignment na attribute 'alltime' to the outer scope of the function
        return onCall
    return onDecorator

# Проверка: 
@timer('==>')                         # listcomp = timer('==>')(listcomp)
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer('==>')
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))

class Test:
    def __init__(self, value, N):
        self.value = value
        self.N = N
    @timer('**')
    def method1(self):
        self.value = [x * 2 for x in range(self.N)]
        brief = self.value[:10]
        brief.append('...')
        print(brief)

X = Test(None, 1000000)
X.__dict__
X.method1()
X.method1.alltime
Test.method1.alltime = 0


##################################################
# Tasks at the end of Chapter 38. Task 2
#Декораторы Private и Public

# file: access.py

'''
Декораторы Private и Public для объявления частных и общедоступных атрибутов.
Управляют доступом к атрибутам, хранящимся в экземпляре или наследуемым
от классов. Декоратор Private объявляет атрибуты, которые недоступны за
пределами декорируемого класса, а декоратор Public объявляет все атрибуты,
которые, наоборот, будут доступны. Внимание: в Python 3.0 эти декораторы
оказывают воздействие только на атрибуты с обычными именами – вызовы методов
перегрузки операторов с именами вида __X__, которые неявно производятся
встроенными операциями, не перехватываются методами __getattr__ и __getattribute__
в классах нового стиля.
Добавьте здесь реализации методов вида __X__ и с их помощью делегируйте выполнение
операций встроенным объектам.
'''
traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        if not __debug__:
            return aClass
        else:
            class onInstance:
                def __init__(self, *args, **kwargs):
                    self.__wrapped = aClass(*args, **kwargs)
                def __getattr__(self, attr):
                    trace('get:', attr)
                    if failIf(attr):
                        raise TypeError('private attribute fetch: ' + attr)
                    else:
                        return getattr(self.__wrapped, attr)
                def __setattr__(self, attr, value):
                    trace('set:', attr, value)
                    if attr == '_onInstance__wrapped':
                        self.__dict__[attr] = value
                    elif failIf(attr):
                        raise TypeError('private attribute change: ' + attr)
                    else:
                        setattr(self.__wrapped, attr, value)
            return onInstance
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))


if __name__ == '__main__':
# Check in interactive shell:
    
    print('1. @Private TEST:')
    @Private('age')       # Person = Private('age')(Person)
    class Person:         # Person = onInstance с информацией о состоянии
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    X = Person('Bob', 40)
    print(X)       # К какомй классу принадлежит X ? (при запуске 'python -O main.py' X = Person(...))
    print(X.name)
    X.name = 'Sue'
    print(X.name)
    try:
        X.age
    except TypeError:
        print('[INFO] TypeError: private attribute fetch: age')
    
    try:
        X.age = 1000
    except TypeError:
        print('[INFO] TypeError: private attribute change: age')
    
    print('\n2. @Public TEST:')
    @Public('name')       # Person = Public('age')(Person)
    class Person:         # Public = onInstance с информацией о состоянии
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    X = Person('Bob', 40)
    print(X)       # К какомй классу принадлежит X ? (при запуске 'python -O main.py' X = Person(...))
    print(X.name)
    X.name = 'Sue'
    print(X.name)
    try:
        X.age
    except TypeError:
        print('[INFO] TypeError: private attribute fetch: age')
    
    try:
        X.age = 1000
    except TypeError:
        print('[INFO] TypeError: private attribute change: age')


##################################################