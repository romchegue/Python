# File person.py

from classtools import AttrDisplay

class Person(AttrDisplay):
    '''
    Creates and processes notes with information about people
    '''
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):                          # The last name is assumed to be the last.
        return self.name.split()[-1]
    def giveRaise(self, percent):                # Percent - is a range 0..1
        self.pay = int(self.pay * (1 + percent)) 

class Manager(Person):
    '''
    Person class version adapted to suit with special requirements
    '''
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
