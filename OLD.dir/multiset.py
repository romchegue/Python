# File: multiset.py

from setwrapper import Set

class MultiSet(Set):
#    def __init__(self, *args):
#        self.data = []
#        self.init_args = args
#        for arg in args:
#            self.concat(arg)
    def intersect(self, *others):
        res = []
        for x in self:  # Сканировать первую последов-ть
            for other in others:  # Для всех остальных аргументов
                if x not in other:  # Элемент присутствует во всех?
                    break  # Нет: прервать цикл
                else:
                    res.append(x)   # Да: добавить элемент в конец
        return Set(res)
    def union(*args):      # self - args[0]
        res = []
        for seq in args:   # Для всех аргументов
            for x in seq:   # Для всех узлов
                if not x in res:
                    res.append(x)     # Добавить новый элемент в результат
        return Set(res)
 

if __name__ == '__main__':
    print("# ms = MultiSet('0adEf')")
    ms = MultiSet('0adEf')
    print("ms =", ms)
    print("ms & [0, 'a', 'A', 'ttt'] =", ms & [0, 'a', 'A', 'ttt'])
    print("ms | [0, 'a', 'A', 'ttt'] =", ms | [0, 'a', 'A', 'ttt'])
    print("ms.intersect('abc', (0, 1, 2, 3, 'a'), 'aaaaaaaaaaaA'):", ms.intersect('abc', (0, 1, 2, 3, 'a'), 'aaaaaaaaaaaA'))
    print("ms.union('abc', (0, 1, 2, 3, 'a'), 'aaaaaaaaaaaA'):", ms.union('abc', (0, 1, 2, 3, 'a'), 'aaaaaaaaaaaA'))

