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
    def __init__(self, name):
        self._name = name
    































































