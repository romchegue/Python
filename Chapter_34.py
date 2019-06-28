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



try:
    import time
    while True:
        print('.')
        time.sleep(1)
except:
    print('caught:', sys.exc_info()[0], '\n')




	