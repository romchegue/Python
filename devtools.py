# file: devtools.py

'''
Файл devtools.py: декоратор функций, выполняющий проверку аргументов на
вхождение в заданный диапазон. Проверяемые аргументы передаются декоратору в
виде именованных аргументов. В фактическом вызове функции аргументы могут
передаваться как в виде позиционных, так и в виде именованных аргументов,
при этом аргументы со значениями по умолчанию могут быть опущены.
Примеры использования приводятся в файле devtools_test.py.
'''

trace = True

def rangetest(**argchecks):   # Проверяемые аргументы с диапазонами
    def onDecorator(func):    # onCall сохраняет func и argchecks
        if not __debug__:     # True - если 'python -O main.py args...'
            return func       # Обертывание только при отладке; иначе 
        else:                 # возвращается оригинальная функция
            import sys
            code = func.__code__ if sys.version_info[0] == 3 else func.func_code
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__
            
            def onCall(*pargs, **kargs):
                # Все аргументы в кортеже pargs сопоставляются с первым N
                # ожидаемыми аргументами по позиции 
                # Остальные либо находятся в словаре kargs, либо опущены, как 
                # аргументы со значениями по умолчанию
                positionals = list(allargs)
                positionals = positionals[:len(pargs)]
                
                for (argname, (low, high)) in argchecks.items():
                    # Для всех аргументов, которые должны быть проверены
                    if argname in kargs:
                        # Аргумент был передан по имени
                        if kargs[argname] < low or kargs[argname] > high:
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                        
                    elif argname in positionals:
                        # Аргумент был передан по позиции
                        position = positionals.index(argname)
                        if pargs[position] < low or pargs[position] > high:
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                        
                    else:
                        # Аргумент не был передан: предполагается, что он 
                        # имеет значение по умолчанию
                        if trace:
                            print('Argument "{0}" dafaulted'.format(argname))
                return func(*pargs, **kargs)              # ОК: вызвать оригинальную функцию
            return onCall
    return onDecorator


