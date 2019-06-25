class ListInherited:
    def __repr__(self):
        return '<Instance of %s, address %s:\n%s>' % (self.__class__.__name__, # Имя класса экземпляра
                                                      id(self), # Адрес экземпляра
                                                      self.__attrnames()) # Список пар name=value            
    def __attrnames(self):
        result = ''
        import types
        for attr in dir(self): # Передать экземпляр функции dir()
            if attr[:2] == '__' and attr[-2:] == '__':    # Пропустить внутренние имена
                result += '\tname %s=<>\n' % attr
            elif isinstance(getattr(self, attr), types.MethodType):
                result += '\tname %s=%s\n' % (attr, '_METHOD_')
            else:
                result += '\tname %s=%s\n' % (attr, getattr(self, attr))
        return result


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
    print(X)

