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

X = C()




















