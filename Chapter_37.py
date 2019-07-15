##################################################
class C:
    def __init__(self, value=None):
        self._x = value
    def getx(self):
        print('get x:')
        return self._x
    def setx(self, value):
        print('set x:', value)
        self._x = value
    def delx(self):
        print('delete x:')
        del self._x
    x = property(fget=getx, fset=setx, fdel=delx, doc="I'm the x property.")

c = C('spam')
c.x
c.x = 'aggs'
c.x
del c.x
c.x
c.x = 'SPAM'


##################################################
class Lol(C):
    def gety(self):
        '''
        This is Lol.gety method =)
        '''
        return self._x
    def sety(self, value=None):
        self._x = value
    def dely(self):
        pass
    y = property(gety, sety, dely)

Y = Lol('SPAM')
Y.__dict__
Y.y
Lol.y.__doc__
Y.y = 1000
del Y.y
Y.__dict__; Y._x


##################################################
# file: ch37_person.py

class Super:
    def __init__(self, name):
        self._name = name
    def getName(self):
        print('fetch...')
        return self._name
    def setName(self, value):
        print('change...')
        self._name = value
    def delName(self):
        print('remove...')
        del self._name
    name = property(fget=getName, fset=setName, fdel=delName, doc='name property docs')  # name = property(name)

class Person(Super):
    pass

if __name__ == '__main__':
    bob = Person('Bob Smith')
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)
    del bob.name
    print('-' * 20)
    sue = Person('Sue Jones')
    print(sue.name)
    print(Person.name.__doc__)


##################################################
class PropSquare:
    def __init__(self, start):
        self.value = start
    def getX(self):
        return self.value ** 2
    def setX(self, value):
        self.value = value
    X = property(getX, setX)

P = PropSquare(3)
Q = PropSquare(32)

print(P.X)
P.X = 4
print(P.X)
print(Q.X)


##################################################
class Person:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):         # name = property(name)
        "name property docs"
        print('fetch...')
        return self._name        
    @name.setter
    def name(self, value):  # name = name.setter(name)
        print('change...')
        self._name = value
    @name.deleter
    def name(self):         # name = name.deleter(name)
        print('remove...')
        del self._name

if __name__ == '__main__':
    bob = Person('Bob Smith')   # Object bob has the managed attribute '_name'
    print(bob.name)             # Will call method 'getter' of property 'name'
    bob.name = 'Robert Smith'   # Will call method 'setter' of property 'name'
    print(bob.name)             
    del bob.name                # Will call method 'deleter' of property 'name'
    print('-' * 20)
    sue = Person('Sue Jones')   # Object sue also inherit property 'name'
    print(sue.name)
    print(Person.name.__doc__)  # Or: help(Person.name)


##################################################
class Descriptor(object):
    'docstring goes here'
    def __init__(self, name):
        self.attrname = name
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')
#        return getattr(instance, self.attrname)
    def __set__(self, instance, value):
        print(self, instance, value, sep='\n')
        raise AttributeError('READ ONLY!')
#        setattr(instance, self.attrname, value)
    def __delete__(self, instance):
        print(self, instance, sep='\n')
#        delattr(instance, self.attrname)


class C(object):
    def __init__(self, start=None):
        self._x = start
    X = Descriptor('X')     # 'X' - managed attribute

I = C('SPAM')


##################################################
class D(object):
    def __get__(*args):
        print('get')

class C:
    a = D()    # 'a' - managed attribute

X = C()


##################################################
class D(object):
    def __get__(*args):
        print('get')
    def __set__(*args):
        raise AttributeError('cannot set')

class C(object):
    a = D()       # 'a' - managed attribute
    def __del__(self):     # !!!!! for 'del' function and garbage collector !!!!!                           
        print('CALLED METHOD', self.__del__)
        del self

X = C()
[C() for i in range(21)]
X


##################################################
class Name(object):
    "name descriptor docs"
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name
    def __set__(self, instance, value):
        print('change...')
        instance._name = value
    def __delete__(self, instance):
        print('remove...')
        del instance._name

class Super(object):
    def __init__(self, name):
        self._name = name
    name = Name() # You should assign descriptor only to attribute of a class (not to self!!!)

class Person(Super):   # Will inherit a decriptor 'name'
    pass

if __name__ == '__main__':
    bob = Person('Bob Smith')
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)
    del bob.name
    print('-' * 20)
    sue = Person('Sue Jones')
    print(sue.name)
    print(Name.__doc__)


##################################################
class Super(object):
    def __init__(self, name):
        self._name = name
    class Name(object):
        "name descriptor docs"
        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name
        def __set__(self, instance, value):
            print('change...')
            instance._name = value
        def __delete__(self, instance):
            print('remove...')
            del instance._name    
    name = Name()

class Person(Super):
    pass

if __name__ == '__main__':
    bob = Person('Bob Smith')
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)
    del bob.name
    print('-' * 20)
    sue = Person('Sue Jones')
    print(sue.name)
    print(Person.Name.__doc__)


##################################################
class DescSquare:
    def __init__(self, start):     # Every descriptor has their own data
        self.value = start
    def __get__(self, instance, owner):   # An operation of getting a value
        return self.value ** 2
    def __set__(self, instance, value):    # An operation of an assignment
        self.value = value

class Client1:
    X = DescSquare(3)

class Client2:
    X = DescSquare(32)

P = Client1()
Q = Client2()

print(P.X)
P.X = 4
print(P.X)
print(Q.X)


##################################################
class Property(object):
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc
    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)  # Pass an instance in the self argument to the access method
    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)
    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

class Person:
    def __init__(self, name):
        self._name = name
    def getName(self):
        print('fetch...')
        return self._name
    def setName(self, value):
        print('change...')
        self._name = value
    def delName(self):
        print('remove...')
        del self._name
    name = Property(fget=getName, fset=setName, fdel=delName, doc='name property docs')  # name = property(name)

lola = Person('Laura Majorgy')


##################################################
class C:
    def __init__(self, name=None):
        self.name = name
    def A(self):
	    return self.B()
    def B(self):
        print(self.name, 'PRINT')
        return self.name

c = C("Marry")
c.A()


##################################################
class  Catcher:
    def __getattr__(self, name):
        print('Get:', name)
    def __setattr__(self, name, value):
        print('Set:', name, value)

X = Catcher()
X.job
X.pay
X.pay = 99


##################################################
class Wrapper:
    def __init__(self, object):
        self.wrapped = object     # Save an object
    def __getattr__(self, attrname):
        print('Trace:', attrname) # Report an attempt to read
        return getattr(self.wrapped, attrname) # Delegate the read operation

class C:
    def __init__(self, name=None):
        self.name = name
    def A(self):
	    return self.B()
    def B(self):
        print(self.name, 'PRINT')
        return self.name

c = C('Polina')
x = Wrapper(c)


##################################################
class Getter(object):
    def __getattribute__(self, name):
        print('fetch attribute', name)
        return object.__getattribute__(self, name)   # Force a call to a superclass method !!!
    def __setattr__(self, name, value):
        print("set attribute 'other' =", value)
        self.__dict__[name] = value   # Using the attribute dictionary !!!
#    def __setattr__(self, name, value): 
#        object.__setattr__(self, name, value)   # Force a call to a superclass method (rearly used)
    def __delattr__(self, name):
        print('remove...')    
        del self.__dict__[name]
#    def __delattr__(self, name):
#        object.__delattr__(self, name)

X = Getter()
X.attr1 = 1000
X.attr2 = 2000
X.__dict__
del X.attr2


##################################################
class Person:
    def __init__(self, name):  # Called when creating a Person()
        self._name = name      # Will call __setattr__ !!!
#    def __getattr__(self, attr):   # Called by obj.udefined
#        if attr == 'name':         # for an absent attribute with the name 'name'
#            print('fetch...')      # 'name' is managed attribute
#            return self._name  # Does not loop: existing attribute
#        else:
#            raise AttributeError(attr)  # Turning to the other non-existent 
#                                        # attributes will call an error
    def __getattribute__(self, attr): # Called by obj.any -
        if attr == 'name':            # - intercepts calls to any names
            print('fetch...')
            attr = '_name'   # Maps to the internal name '_name'
        return object.__getattribute__(self, attr)  # To prevent looping 
    def __setattr__(self, attr, value): # Called by obj.any = value
        if attr == 'name':       # 'name' is managed attribute
            print('change...')
            attr = '_name'     # The internal name of the attribute
        self.__dict__[attr] = value   # To prevent looping
    def __delattr__(self, attr):   # Called by del obj.name
        if attr == 'name':       # 'name' is managed attribute
            print('remove...')
            attr = '_name'
        del self.__dict__[attr]  # To prevent looping
<<<<<<< HEAD
=======

if __name__ == '__main__':
    bob = Person('Bob Smith')  # 'name' is managed attribute
    print(bob.name)            # Will call __getattr__
    bob.name = 'Robert Smith'  # Will call __setattr__
    print(bob.name)
    del bob.name               # Will call __delattr__
    print('-' * 20)
    sue = Person('Sue Jones')    
    print(sue.name)


##################################################





>>>>>>> 0a999842c1ef89e23fce1990c6b7ec70b5a88cae

if __name__ == '__main__':
    bob = Person('Bob Smith')  # 'name' is managed attribute
    print(bob.name)            # Will call __getattr__
    bob.name = 'Robert Smith'  # Will call __setattr__
    print(bob.name)
    del bob.name               # Will call __delattr__
    print('-' * 20)
    sue = Person('Sue Jones')    
    print(sue.name)


##################################################
class AttrSquare:
    def __init__(self, start):
        self.value = start     # Will call __setattr__ !!!
    def __getattr__(self, attr):  # Called by obj.udefined
        if attr == 'X':
             return self.value ** 2  # Attribute 'value' is existing
        else:
            raise AttributeError(attr)
    def __setattr__(self, attr, value):  # Called by obj.any = value
        if attr == 'X':
            attr = 'value'
        self.__dict__[attr] = value

A = AttrSquare(3)   # 2 istance of the class with operator overloading methods
B = AttrSquare(32)  # Every instance will save their own data  


##################################################
class AttrSquare:
    def __init__(self, start):
        self.value = start     # Will call __setattr__ !!!
#    def __getattribute__(self, attr):  # Called by obj.any
#        if attr == 'X':
#            return self.value ** 2  # Method '__getattribute__' - 
#        else:                       # will be called again !!!
#            return object.__getattribute__(self, attr)
    def __getattribute__(self, attr):  # Called by obj.any
        if attr == 'X':
            return object.__getattribute__(self, 'value') ** 2  # Method '__getattribute__' - 
        else:                                                   # will be called again !!!
            return object.__getattribute__(self, attr)    
    def __setattr__(self, attr, value):  # Called by obj.any = value
        if attr == 'X':
            attr = 'value'
        object.__setattr__(self, attr, value)

A = AttrSquare(3)   # 2 istance of the class with operator overloading methods
B = AttrSquare(32)  # Every instance will save their own data  


##################################################
class GetAttr(object):
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    def __getattr__(self, attr):
        if attr == 'attr3':
            print('get: ' + attr)
            return 3
        else:
            raise AttributeError(attr)

X = GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)

print('-' * 40)

class GetAttribute(object):
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    def __getattribute__(self, attr):
        print('get: ' + attr)
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)

X = GetAttribute()
print(X.attr1)
print(X.attr2)
print(X.attr3)

            
##################################################
class Powers:
    def __init__(self, square, cube):        
        self._square = square
        self._cube = cube
    def getSquare(self):
        return self._square ** 2
    def setSquare(self, value):
        self._square = value
    square = property(getSquare, setSquare)
    def getCube(self):
        return self._cube ** 3
    cube = property(getCube)

X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)


##################################################
class DescSquare:
    def __get__(self, instance, owner):
        return instance._square ** 2
    def __set__(self, instance, value):
        instance._square = value

class DescCube:
    def __get__(self, instance, owner):
        return instance._cube ** 3

class Powers:
    square = DescSquare()
    cube = DescCube()
    def __init__(self, square, cube):        
        self._square = square   # 'self.square = square' will also work - 
        self._cube = cube       # - because it will call 'DescSquare.__set__'

X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)


##################################################
class Powers:
    def __init__(self, square, cube):        
        self._square = square
        self._cube = cube
    def __getattr__(self, name):
        if name == 'square':
            return self._square ** 2
        elif name == 'cube':
            return self._cube ** 3
        else:
            raise AttributeError('unknown attribute: ' + name)
    def __setattr__(self, name, value):
        if name == 'square':
            name = '_square'
#        object.__setattr__(self, name, value)
        self.__dict__[name] = value

X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)


##################################################
class Powers:
    def __init__(self, square, cube):        
        self._square = square
        self._cube = cube
    def __getattribute__(self, name):
        if name == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif name == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name == 'square':
            name = '_square'
#        object.__setattr__(self, name, value)
        self.__dict__[name] = value

X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)


##################################################
# file: getattr.py 

class GetAttr:
    eggs = 88
    def __init__(self):
        self.spam = 77
    def __len__(self):
        print('__len__: 42')	
        return 42
    def __getattr__(self, attr):
        print('getattr: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None

class GetAttribute:
    eggs = 88
    def __init__(self):
        self.spam = 77
    def __len__(self):
        print('__len__: 42')	
        return 42
    def __getattribute__(self, attr):		
        print('getattribute: ' + attr)
        if attr == '__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None

for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(50, '='))
	X = Class()
	X.eggs
	X.spam
	X.other
	len(X)
	try:
	    X[0]
    except:
        print('fail []')
	try:
	    X + 99
    except:
        print('fail +')    
	try:
	    X()
    except:
        print('fail ()')
    X.__call__()
    print(X.__str__())
    print(X)


##################################################
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __str__(self):
        return '[Person: {0}, {1}]'.format(self.name, self.pay)

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)
    def giveRaise(self, percent, bonus=0.10):
        self.person.giveRaise(percent + bonus)
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    def __str__(self):               # Must redefine in Python 3.x 
        return str(self.person)

if __name__ == '__main__':
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Hanks', 50000)   # Manager.__init__
    print(tom.lastName())               # Manager.__getattr__ ---> Person.lastName
    tom.giveRaise(.10)                  # Manager.giveRaise ---> Person.giveRaise
    print(tom)                          # Manager.__str__ ---> Person.__str__


##################################################











