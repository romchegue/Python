# File: test.py

class Spam:
    numInstances = 0         # Monitors the number of instances        
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(cls):
        print('Number of instances:', cls.numInstances, cls)
    printNumInstances = classmethod(printNumInstances)

class Sub(Spam):
    def printNumInstances(cls):           # Overrides the class method
        print('Extra stuff...', cls)      
        Spam.printNumInstances()          # But calls an original
    printNumInstances = classmethod(printNumInstances)

class Other(Spam): pass      # Inherits class method
              
