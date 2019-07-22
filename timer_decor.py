# file: timer_decor.py

import time

class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        elapsed = time.time() - start
        self.alltime += elapsed
#        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        print('{0}: {1:.5f}, {2:.5f}'.format(self.func.__name__, elapsed, self.alltime))
        return result

@timer
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer
def mapcall(N):
    return map((lambda x: x * 2), range(N))


result = listcomp(5)
listcomp(50000)
listcomp(500000)
listcomp(1000000)
print(result)
print('allTime = {0}'.format(listcomp.alltime))

print('')
result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print('allTime = {0}'.format(mapcall.alltime))

print('map/comp = {0}'.format(round(mapcall.alltime / listcomp.alltime, 3)))

