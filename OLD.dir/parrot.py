# File: parrot.py

class Printer:
    def line(self):
        print(self.name + ':', repr(self.says()))

class Customer(Printer):
    name = 'customer'
    def says(self):
        return "that's one ex-bird!"

class Clerk(Printer):
    name = 'clerk'
    def says(self):
        return "no it isn't..."

class Parrot(Printer):
    name = 'parrot'
    def says(self):
        return None
       
class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.subject = Parrot()
    def action(self):
        self.customer.line()
        self.clerk.line()
        self.subject.line()

if __name__ == '__main__':
    Scene().action()

