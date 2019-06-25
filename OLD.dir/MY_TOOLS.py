# File: MY_TOOLS.py

#__all__ = ['dirprinter', 'dircomparator', 'printer']

def dirprinter(arg=None):
    '''
    Function dirprinter(arg) prints dir(arg) in the convenient format.
    Example: dirprinter(X)
    '''
    def max_len(dir_list):
        '''
        Function max_len(dir_list), where dir_list is supposed list dir(smth)
        returns the maximum lengths (integer) of an item in the dir_list. 
        Example: max_len(X) --> mxln
        '''
        mxln = 0 
        for i in dir_list:       
            if len(i) > mxln:
                mxln = len(i)            
        return  mxln   
    if arg == None:
        print('WARNING!!!\n' + dirprinter.__doc__ + '\nPLEASE TRY AGAIN.')
    elif __name__ == '__main__' and type(arg) == list and '__builtins__' in arg:
        mx = max_len(arg)
        print('[The list dir() of the __main__ module]:\n')
        for i in arg: 
            print('|{0:{1}}| {2}'.format(i, mx, globals()[i]))
    else:
        mx = max_len(dir(arg))
        print("[The list dir() of {0} ({1})\nModule's __name__ = {2}]:\n".format(repr(arg), 
                                                                                           type(arg), 
                                                                                            __name__))
        for i in dir(arg):
            print('|{0:{1}}| {2}'.format(i, mx, getattr(arg, i)))                  #OLD: print('|{0:{1}}|'.format(i, mx))


def dir_comp(x, y):
    '''
    Function dircomparator(x, y) prints differences between attributes 
    and methods of objects x and y by comparison of dir(x) and dir(y).
    Example: dircomparator(A, B)
    '''
    res = []
    for i in dir(x):
        if not i in dir(y):
            res.append(i)
            print(i)
    print('- - -')
    return res


def printer(x):
    '''
    Function printer(x) just prints the contents of the argument in a human-readable form
    Example: printer(X)
    '''
    def max_len(iter_arg):
        '''
        Function max_len(iter_arg), where iter_arg is supposed iterable object like list, 
        tuple, set, dictionary etc. returns the maximum lengths (integer) of an item in 
        the iter_arg. 
        Example: max_len(X) --> mxln
        '''
        mxln = 0 
        for i in iter_arg:       
            if len(i) > mxln:
                mxln = len(i)            
        return  mxln
    for i in x:
        mx = max_len(x)
        print('|{0:{1}}|'.format(i, mx))


def dircleaner(*args):
    '''
    Function cleaner(*args) cleans the list dir() of the '__main__' module.
    If there are no argumets present - cleans whole list dir().
    Example: cleaner('x', 'y', 'func')
    '''
    start_list = ['dircleaner', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
    if args == ():
        dir_lst = list(globals().keys())[:]
        for i in dir_lst:
            if i not in start_list:
                del globals()[i]
        print('---\nCleaned the whole list of attributes dir() of global module.')
    else:
        for i in args:
            del globals()[i]
        print('---\nCleaned the list {0} of attributes dir() of global module.'.format(args))


# Self-tests:
if __name__ == '__main__':
    print('      \n1. TESTING OF dirprinter(arg) FUNCTION:\n')
    dirprinter()
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n')
    dirprinter('SPAM')
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n')
    dirprinter(dir())
    print('      \n2. TESTING OF dir_comp(x, y) FUNCTION:\n')
    dir_comp('', 1)
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n')
    dir_comp(2, 1)
    print('      \n3. TESTING OF printer(x) FUNCTION:\n')
    printer(['A', 'B', 'Ccccccc'])
    print('      \n4. TESTING OF dircleaner(*args) FUNCTION:\n')
    A, B, C, D = 0, {1: 500}, '2', [3]
    print("A, B, C, D =", (A, B, C, D))
    print('dir() ---> ', dir())
    dircleaner('A')
    dircleaner('B')
    dircleaner()
    print('RESULT dir() ---> ', dir())
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n')

