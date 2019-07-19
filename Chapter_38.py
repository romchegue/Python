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
    def __init__(self, func):   # at the stage of decoration @:
        self.calls = 0          # saves orginal function 'func'
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
class tracer:
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
        print("[TEST] tracer.__call__:", self, *args, **kwargs)
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):    # Вызывается при обращении к методу
        print("[TEST] tracer.__get__:", instance, owner)
        def wrapper(*args, **kwargs):      # Сохраняет оба экземпляра 
            print("[TEST] tracer.__get__.wrapper:", *args, **kwargs)
            return self(instance, *args, **kwargs)   # Вызовет __call__ 		
        return wrapper
