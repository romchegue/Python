import sys, mytimer
reps = 10000
repslist = range(reps) 

from math import sqrt
def mathsqrt():
    return sqrt(1111111)
    
def x_power05():
    return 1111111 ** 0.5

def power_x05():
    return pow(1111111, 0.5)
	
print(sys.version)
for tester in (mytimer.timer, mytimer.best):
    print('<%s>' % tester.__name__)
    for test in (mathsqrt, x_power05, power_x05):
        elapsed, result = tester(test)
        print ('-' * 45)
        print ('%-9s: %.10f => %s' % (test.__name__, elapsed, result))

