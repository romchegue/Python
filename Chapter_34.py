# file: Chapter_34.py

def exceptor():
    x = input('INPUT SMTH: ')
    try:
        print(eval(x))
    except Exception:
        import sys
        return sys.exc_info()       # Get the last instance of an exception 


def exceptor1():
    x = input('INPUT SMTH: ')
    try:
        print(eval(x))
    except Exception as X:                        # X - a raised instance
        return (X.__class__, X, X.__traceback__)  # The same as sys.exc_info()




###############################
class ExcExplorer:
    cls_tree = []
    def basesDict(class_object, c=0):
        if c == 0:
            ExcExplorer.cls_tree = []             # Clear a list of results 
        ExcExplorer.cls_tree.append(class_object)
        print('.' * c + repr(class_object))
        for cls in class_object.__bases__:
            ExcExplorer.basesDict(cls, c + 3)
    basesDict = staticmethod(basesDict)


def lister(x):
    try:
        I = ExcExplorer()
        x.__bases__
        I.basesDict(x)
    except AttributeError:
        import sys
        print('caught:', sys.exc_info()[0], '\n')
        I.basesDict(x.__class__)
    print()
    return I.cls_tree
###############################

try:
    import time
    while True:
        print('.')
        time.sleep(1)
except:
    print('caught:', sys.exc_info()[0], '\n')


class MyBad(Exception):
    def __str__(self):
        return 'Got: {0}\nAlways look on the bright side of life...'.format(self.args)

try:
    raise MyBad()
except MyBad as X:
    print(X)



class FormatError(Exception):
    logfile = 'formaterror.txt'
    def __init__(self, line, file):
        self.line = line
        self.file = file
    def logerror(self):
        log = open(self.logfile, 'a')
        print('Error at', self.line, self.line, file=log)

def parser():
    raise FormatError(40, 'spam.txt')

try:
    parser()
except FormatError as exc:
    exc.logerror()















	