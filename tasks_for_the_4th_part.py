# Task 1:
def func(arg):
    print(arg)


# Task 2:
def adder(arg1, arg2):
    print(arg1 + arg2)
    return arg1 + arg2

adder('abc', 'ABC')
adder(['a', 'b', 'c'], ['A', 'B', 'C'])
adder(1.0038454, 2.47569867)


# Task 3:
def adder(*pargs):
    if type(pargs[0]) in (int, float, complex):
        res = 0
    else:
        res = pargs[0][:0]
    for i in pargs:
        res += i
    return res

def adder2(*args):             # From answers
    sum = args[0]
    for next in args[1:]:
        sum += next
    return sum
	
adder('abc', 'ABC')
adder(['a', 'b', 'c'], ['A', 'B', 'C'])
adder(1.0038454, 2.47569867)


# Task 4:
def adder1(**kargs):
    good = kargs.pop('good', 1)
    bad = kargs.pop('bad', 2)
    ugly = kargs.pop('ugly', 3)
    D = {}
    D['good'] = good
    D['bad'] = bad
    D['ugly'] = ugly
    D.update(kargs)
 #   print(D)
    if type(D['good']) in (int, float, complex):
        res = 0
    else:
        res = D['good'][:0]
    for key, value in D.items():
        res += value
    print('\ntype =', type(res), '\n')
    return res
#____________________________________________________
def adder2(**kargs):
    good = kargs.pop('good', 1)
    bad = kargs.pop('bad', 2)
    ugly = kargs.pop('ugly', 3)
    D = {}
    D['good'] = good
    D['bad'] = bad
    D['ugly'] = ugly
    D.update(kargs)
    print(D)
    sum = D[list(D.keys())[0]]
    for next in list(D.keys())[1:]:
        sum += D[next]
    print('\ntype =', type(sum), '\n')
    return sum

	
# Task 5:
def copyDict(D):
    D1 = {}
    for key in D.keys():
        if type(D[key]) in (int, float, complex, str, tuple, dict):
            D1[key] = D[key]
        else:
            D1[key] = D[key][:]
    return(D1)


# Task 6:
def addDict(dict1, dict2):
    # For dictionaries:
    if type(dict1) == dict:
        D = {}
        for key in dict1:
            if key in dict2:
                flag = input('For {K} choice {0} - input 0, if {1} - input smth: '.format(dict1[key], dict2[key], K=key))
                if flag == '0': 
                    D[key] = dict1[key]
                else: 
                    D[key] = dict2[key]
        for key in dict2:
            if key not in dict1:
                D[key] = dict2[key]
    # For lists:
    elif type(dict1) == list:
        D = []
        for i in dict1:
            D.append(i)
        for j in dict2:
            if j not in dict1: # Do not add duplicate values
                D.append(j)
    return(D)


# Task 8:
def prime(y):
    if y <= 1:
	    print(y, 'is not prime')
    else:
        x = y // 2
        while x > 1:
            if y % x == 0: 
                print(y, 'has factor', x)
                break
            x -= 1
        else: 
            print(y, 'is prime')
 
prime(13)
prime(13.0)
prime(15)
prime(15.0)
#____________________________________________________
def prime_new(y):
    if y <= 1:
	    print(y, 'is not prime')
    else:
        x = y // 2
        for x in range(x, 1, -1):
            if y % x == 0: 
                print(y, 'has factor', x)
                break
        else: 
            print(y, 'is prime')

prime(13)
prime(13.0)
prime(15)
prime(15.0)


# Task 9:
L = [2, 4, 9, 16, 25]

def square_root(L):
    from math import sqrt
    res = []
    for x in L:
        res.append(sqrt(x))
    return(res)

def square_root1(L):
    from math import sqrt
    return list(map(sqrt, L))

def square_root2(L):
    from math import sqrt
    return [sqrt(x) for x in L] 


# Task 10:
mport sys, mytimer
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
        print ('-' * 35)
        print ('%-9s: %.5f => %s' % (test.__name__, elapsed, result))

#____________________________________________________

reps = 10000
repslist = range(reps) 
def dict_maker():
    res = {}
    for x in repslist:
        res[x] = x + 1
    return res

def dict_maker_gen():
    return {x: x + 1 for x in repslist}

from mytimer import best
'{0:.7f}; {1:.7f}'.format(best(dict_maker)[0], best(dict_maker_gen)[0])