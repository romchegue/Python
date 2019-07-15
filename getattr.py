# file: getattr.py

class GetAttr:
    eggs = 88
    def __init__(self):
        self.spam = 77
    def __len__(self):
        print('__len__: 42')
        return 42
    def __getattr__(self, attr):   # Called by 'obj.any'  
        print('geattr: ' + attr)   # if 'any' not in 'dir(obj)' !!!
        if attr == '__str__':
            return lambda *args: '[GetAttr str]'
        else:
            return lambda *args: None

class GetAttribute(object):
    eggs = 88
    def __init__(self):
        self.spam = 77
    def __len__(self):
        print('__len__: 42')
        return 42
    def __getattribute__(self, attr):
        print('getattribute: ' + attr)
        if attr == '__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None

for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(50, '='))
    X = Class()
    X.eggs
    X.spam
    X.other
    len(X)  # __len__
    try:
        X[0]
    except:
        print('fail []')
    try:
        X + 99   # __add__ ?
    except:
        print('fail +')
    try:
        X()     # __call__ ?
    except:
        print('fail ()')
    X.__call__()  # __call__ - explicit call 
    print(X.__str__())   # __str__? - inherited from 'type' !!!
    print(X)       # __str__ - implicit call
