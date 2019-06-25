# File testmixin.py
from lister import * # Импортировать инструментальные классы

class Super:
    def __init__(self): # Метод __init__ суперкласса
        self.data1 = 'spam' # Создать атрибуты экземпляра
    def ham(self):
        pass

class Sub(Super, ListInherited): # Подмешать методы ham и __str__
    def __init__(self): # Инструментальные классы имеют доступ к self
        Super.__init__(self)
        self.data2 = 'eggs' # Добавить атрибуты экземпляра
        self.data3 = 42
    def spam(self): # Определить еще один метод
        pass

if __name__ == '__main__':
    X = Sub()
    print(X) # Вызовет подмешанный метод __str__

