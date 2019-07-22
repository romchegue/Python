# file: mytools.py

import time

def timer(label='', trace=True):    # Arguments of the decorator saves
    class Timer:                    # class Timer is the actual decorator 
        def __init__(self, func):   # At the stage of decoration, 
            self.func = func        # the decorated function is preserved
            self.alltime = 0
        def __call__(self, *args, **kwargs):  # When called: the original is called    
            start = time.time()
            result = self.func(*args, **kwargs)
            elapsed = time.time() - start
            self.alltime += elapsed
            if trace:
                format = '{0} {1}: {2:.5f}, {3:.5f}'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format.format(*values))
            return result
    return Timer

@timer('==>')                         # listcomp = timer('==>')(listcomp)
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer('==>')
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))

