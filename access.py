# file: access.py

'''
Декораторы Private и Public для объявления частных и общедоступных атрибутов.
Управляют доступом к атрибутам, хранящимся в экземпляре или наследуемым
от классов. Декоратор Private объявляет атрибуты, которые недоступны за
пределами декорируемого класса, а декоратор Public объявляет все атрибуты,
которые, наоборот, будут доступны. Внимание: в Python 3.0 эти декораторы
оказывают воздействие только на атрибуты с обычными именами – вызовы методов
перегрузки операторов с именами вида __X__, которые неявно производятся
встроенными операциями, не перехватываются методами __getattr__ и __getattribute__
в классах нового стиля.
Добавьте здесь реализации методов вида __X__ и с их помощью делегируйте выполнение
операций встроенным объектам.
'''
traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        if not __debug__:
            return aClass
        else:
            class onInstance:
                def __init__(self, *args, **kwargs):
                    self.__wrapped = aClass(*args, **kwargs)
                def __getattr__(self, attr):
                    trace('get:', attr)
                    if failIf(attr):
                        raise TypeError('private attribute fetch: ' + attr)
                    else:
                        return getattr(self.__wrapped, attr)
                def __setattr__(self, attr, value):
                    trace('set:', attr, value)
                    if attr == '_onInstance__wrapped':
                        self.__dict__[attr] = value
                    elif failIf(attr):
                        raise TypeError('private attribute change: ' + attr)
                    else:
                        setattr(self.__wrapped, attr, value)
            return onInstance
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))


if __name__ == '__main__':
# Check in interactive shell:
    
    print('1. @Private TEST:')
    @Private('age')       # Person = Private('age')(Person)
    class Person:         # Person = onInstance с информацией о состоянии 
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    X = Person('Bob', 40)
    print(X)       # К какомй классу принадлежит X ? (при запуске 'python -O main.py' X = Person(...))
    print(X.name)
    X.name = 'Sue'
    print(X.name)
    try:
        X.age
    except TypeError:
        print('[INFO] TypeError: private attribute fetch: age')
    
    try:
        X.age = 1000
    except TypeError:
        print('[INFO] TypeError: private attribute change: age')
    
    print('\n2. @Public TEST:')
    @Public('name')       # Person = Public('age')(Person)
    class Person:         # Public = onInstance с информацией о состоянии 
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    X = Person('Bob', 40)
    print(X)       # К какомй классу принадлежит X ? (при запуске 'python -O main.py' X = Person(...))
    print(X.name)
    X.name = 'Sue'
    print(X.name)
    try:
        X.age
    except TypeError:
        print('[INFO] TypeError: private attribute fetch: age')
    
    try:
        X.age = 1000
    except TypeError:
        print('[INFO] TypeError: private attribute change: age')
