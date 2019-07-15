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
    name = property(fget=getName, fset=setName, fdel=delName, doc='name property docs')

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
