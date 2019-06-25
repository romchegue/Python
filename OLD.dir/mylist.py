class MyList:
    def meth_print(meth_name, index=None, item=None):
        log_message = "log message: called {module}.MyList.{method}".format(module=__name__, method=meth_name)
        if index != None:
            log_message += ', index = {0}'.format(index)
        if item != None:
            log_message += ', \nitem = {0}'.format(item)
        print('###', log_message, '###')
    meth_print = staticmethod(meth_print)
    def __init__(self, value=[]):
        '''Initialize self ---> self.data = value[:]'''
        MyList.meth_print(meth_name='__init__', item=value)
        self.data = []
        for x in value:        # value can be an any iterable object                
            self.data.append(x)
#    def __init__(self, value=[]):
#        '''Initialize self ---> self.data = value[:]'''
#        MyList.meth_print(meth_name='__init__', item=value)
#        self.data = value[:]
#    def __init__(self, *args, **kwargs):    # ALTERNATIVE
#        MyList.meth_print(meth_name='__init__', item=(args, kwargs))
#        self.data = []
#        for arg in args:
#            self.data.append(arg)
#        for val in kwargs.values():
#            self.data.append(val)
#        print('{0}.data = {1}'.format(self, self.data))
    def __getattr__(self, name):
        return getattr(self.data, name)
    def __repr__(self):
        MyList.meth_print(meth_name='__repr__')
        return 'MyList: ' + repr(self.data)
    def __add__(self, value):
        MyList.meth_print(meth_name='__add__', item=value)
        return MyList(self.data + value)
    def __contains__(self, item):
        MyList.meth_print(meth_name='__contains__', item=item)
        return item in self.data
    def __delitem__(self, index):
        MyList.meth_print(meth_name='__delitem__', index=index) 
        del self.data[index]
    def __eq__(self, value):
        MyList.meth_print(meth_name='__eq__', item=value) 
        return self.data == value
    def __getitem__(self, index):
        MyList.meth_print(meth_name='__getitem__', index=index)
        return self.data[index]
    def __iadd__(self, value):
        MyList.meth_print(meth_name='__iadd__', item=value)
        return MyList(self.data + value)
    def __imul__(self, value):
        MyList.meth_print(meth_name='__imul__', item=value)
        return MyList(self.data * value)
    def __iter__(self):
        MyList.meth_print(meth_name='__iter__')
        return iter(self.data)
    def __len__(self):
        MyList.meth_print(meth_name='__len__')
        return len(self.data)
    def __mul__(self, value):
        MyList.meth_print(meth_name='__mul__', item=value)
        return MyList(self.data * value)
    def __radd__(self, value):
        MyList.meth_print(meth_name='__radd__', item=value)
        return MyList(value + self.data)
    def __reversed__(self):
        MyList.meth_print(meth_name='__reversed__')
        return reversed(self.data)
    def __rmul__(self, value):
        MyList.meth_print(meth_name='__rmul__', item=value)
        return MyList(self.data * value)
    def __setitem__(self, index, value):
        MyList.meth_print(meth_name='__setitem__', index=index, item=value)
        self.data[index] = value
    def append(self, value):
        MyList.meth_print(meth_name='append', item=value)
        self.data.append(value)
    """
    def clear(self):
        MyList.meth_print(meth_name='clear')
        self.data.clear()
    def copy(self):
        MyList.meth_print(meth_name='copy')
        return MyList(self.data[:])
    def count(self, value):
        MyList.meth_print(meth_name='count', item=value)
        return self.data.count(value)		
    def extend(self, iterable):
        MyList.meth_print(meth_name='extend', item=iterable)
        self.data.extend(iterable)
    def index(self, value, start=0, stop=9223372036854775807): 
        MyList.meth_print(meth_name='index', index=(start, stop), item=value)
        return self.data.index(value, start, stop)
    def insert(self, index, value): 
        MyList.meth_print(meth_name='insert', index=index, item=value)
        self.data.insert(index, value)
    def pop(self, index=-1): 
        MyList.meth_print(meth_name='pop', index=index)
        return self.data.pop(index)
    def remove(self, value):
        MyList.meth_print(meth_name='remove', item=value)
        self.data.remove(value)
    def reverse(self):
        MyList.meth_print(meth_name='reverse')
        self.data.reverse()
    def sort(self, key=None, reverse=False):
        MyList.meth_print(meth_name='sort', item='key={0}, reverse={1}'.format(key, reverse))
        self.data.sort(key, reverse)
    """


class MyListSub(MyList):   # Inherits class MyList from the task 2
    count_of_inst = 0
    meth_calls = 0
    def __init__(self, value=[]):
        MyListSub.count_of_inst += 1
        self.add_calls = 0
        MyList.__init__(self, value)
    def __getattribute__(self, name):
        if name[:2] == '__' and name[-2:] == '__':
            print('Called method', name)
    def countPrinter(self):
        print('Count of created instances:', count_of_inst)
        print('Operation "+" called {0} times'.format())
    def __add__(self, other):
        self.add_calls += 1
        MyList.__add__(self, other)


