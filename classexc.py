# file: classexc.py

class General(Exception): pass

class Specific1(General): pass

class Specific2(General): pass

def raiser0():
    X = General()  # Raises an instance of an exception superclass
    raise X

def raiser1():
    X = Specific1()  # Raises an instance of an exception subclass
    raise X

def raiser2():
    X = Specific2()  # Raises an instance of another exception subclass
    raise X

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:  # Catch exceptions General and any of its subclasses
        import sys
        print('caught:', sys.exc_info()[0])
