# file: private38.py
# Реализация частных атрибутов
'''
Ограничение на чтение значений частных атрибутов экземпляров классов.
Примеры использования приводятся в программном коде самопроверки, в конце.
Декоратор действует как: Doubler = Private('data', 'size')(Doubler).
Функция Private возвращает onDecorator, onDecorator возвращает onInstance,
а в каждый экземпляр onInstance встраивается экземпляр Doubler.
'''
traceMe = False
def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')

def Private(*privates):         # privates - в объемлющей области видимости
    def onDecorator(aClass):    # aClass - в объемлющей области видимости
        class onInstance:       # Обертывает экземпляр атрибута
            def __init__(self, *args, **kwargs):
                self.wrapped = aClass(*args, **kwargs)
            def __getattr__(self, attr):       # Для собственных атрибутов getattr не вызывается 
                trace('get:', attr)          # Другие, как предполагается, принадлежат 
                if attr in privates:         # обернутому объекту
                    raise TypeError('private attrribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)
            def __setattr__(self, attr, value):   # Доступ извне
                trace('set:', attr, value)     # Другие обрабатываются нормально
                if attr == 'wrapped':        # Разрешить доступ к своим атрибутам (wrapped)
                    self.__dict__[attr] = value		# Избежать зацикливания		
                elif attr in privates:
                    raise TypeError('private attrribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)   # Атрибуты обернутого объекта. Или можно исп. __dict__
        return onInstance
    return onDecorator

if __name__ == '__main__':
    traceMe = True
    
    @Private('data', 'size')     # Doubler = Private('data', 'size')(Doubler)
    class Doubler:
        def __init__(self, label, start):
            self.label = label    # Доступ изнутри класса
            self.data = start     # Не перехватываетсяЖ обрабатывается как обычно
        def size(self):
            return len(self.data)       # Методы выполняются без проверки, потому
        def double(self):                # что ограничение доступа не наследуется
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        def display(self):
            print('%s => %s' % (self.label, self.data))

    X = Doubler('X is', [1, 2, 3])
    Y = Doubler('Y is', [-10, -20, -30])
    
    # Все следующие попытки оканчиваются успехом
    
    print(X.label)                        # Доступ извне класса
    X.display(); X.double(); X.display()  # Перехватывается: проверяется, делегируется
    print(Y.label)
    Y.display(); Y.double()
    Y.label = 'Spam'
    Y.display()
    
    # Все следующие попытки терпят неудачу
    '''
    print(X.size())    # Выведет "TypeError: private attrribute fetch: size"
    print(X.data)
    X.data = [1, 1, 1]
    X.size = lambda S: 0
    print(Y.data)
    print(Y.size())
    '''

