# File: zoo.py

class Animal:
    def reply(self):
        self.speak()
    def speak(self):
        print("WARNING: object {0} doesn't have method 'speak'".format(self))
    def printer(self, cls):
        print('This is method:   {0}.speak\nShould be method: {1}.speak'.format(cls.__name__, self.__class__.__name__))


class Mammal(Animal):
    def speak(self):
        self.printer(Mammal)

class Cat(Mammal):
    def speak(self):
        self.printer(Cat)

class Dog(Mammal):
    def speak(self):
        self.printer(Dog)

class Primate(Mammal):
    def speak(self):
        self.printer(Primate)

class Hacker(Primate):
    def speak(self):
        self.printer(Hacker)


if __name__ == '__main__':
    a = Animal()
    m = Mammal()
    c = Cat()
    d = Dog()
    p = Primate()
    h = Hacker()
    for inst in (a, m, c, d, p, h):
        print('OBJECT:', inst)
        inst.reply()
        print('- - - - - - - - - - - - - - - - - - - - - - \n')
    del Hacker.speak
    print('Hacker.speak was deleted')
    h.reply()

