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
















