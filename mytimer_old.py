import time
reps = 1000
repslist = range(reps)

def timer(func, *pargs, **kargs):
    start = time.process_time()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.process_time() - start
    return (elapsed, ret)

"""
import sys, mytimer
reps = 10000
repslist = range(reps) 

def forLoop():
    res = []
    for x in repslist:
        res.append(x + 1)
    return res

def listComp():
    return [x + 1 for x in repslist]

def mapCall():
    return list(map((lambda x: x + 1), repslist))

def genExpr():
    return list(x + 1 for x in repslist) 

def genFunc():
    def gen():
        for x in repslist:
            yield (x + 1)
    return list(gen())

print(sys.version)
for tester in (mytimer.timer, mytimer.best):
    print('<%s>' % tester.__name__)
    for test in (forLoop, listComp, mapCall, genExpr, genFunc):
        elapsed, result = tester(test)
        print ('-' * 35)
        print ('%-9s: %.5f => [%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))

"""