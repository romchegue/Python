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
        ExcExplorer.cls_tree.append(class_object)
        print('.' * c + repr(class_object))
        for cls in class_object.__bases__:
            ExcExplorer.basesDict(cls, c + 3)
    basesDict = staticmethod(basesDict)


def lister(x):
    try:
        ExcExplorer.basesDict(x)
    except AttributeError as TE:
        print('caught', TE)
        res[x] = x.__class__
        lister(x.__class__)
    print('res =', res)
    return res


class ExcExplorer:
    def __init__(self):
        self.cls_tree = []
    cls_tree = []
    def basesDict(self, clss='self.__class__', c=0):
        self.cls_tree.append(clss)
        print('.' * c + repr(clss))
        for C in self.__class__.__bases__:
            ExcExplorer.basesDict(self, C, c + 3)


	