# Task 1.a:
'''
| This code displays ASCII-codes 
| of all characters in the string S

'''
while True:
    S = input("Input a string of symbols or 'stop' to break: ")
    if S == 'stop': 
	    break
    for i in S:
        print(ord(i), end=' ')
    print('\n' * 2)

	
# Task 1.b:
'''
| This code displays a sum of ASCII-codes 
| of all characters in the string S

'''
while True:
    S = input("Input a string of symbols or 'stop' to break: ")
    if S == 'stop': 
	    break
    res = 0
    for i in S:
        res += ord(i)
    print(res, '\n')

	
# Task 1.c:
'''
| This code returns a list of ASCII-codes 
| of all characters in the string S

'''
def odrlist(S=''):
    '''
    # This function returns a list of ASCII-codes 
    # of all characters in the string S. 
	# - If S is default, the function prefers to input 
	# a string (ex.: ordlist()).
	# - If S is passed to the function, it will be 
    # processed and returned.
	
    '''
    if S == '':
        S = input("Input a string of symbols: ")
    L = [ord(i) for i in S]
    return(L)


# Task 2:
for i in range(50): print('hello %d\n\a' % i)


# Task 3:
'''
| Dictionary sorting.

'''
D = {'d': 3, 'e': 4, 'a': 0, 'b': 1, 'c': 2}

for key in sorted(D):				# 1st version
    print(key, D[key])

K = list(D.keys())				# 2nd version
K.sort()
for key in K:
    print(key, D[key])


# Task 4.a:
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0
while i < len(L):
    if 2 ** X == L[i]:
        print(2 ** X, 'was found at index', i)
        break
    i = i+1
else:
    print(2 ** X, 'not found')


# Task 4.b: 
L = [1, 2, 4, 8, 16, 32, 64]
X = 5

for i in L:
    if 2 ** X == i:
        print(2 ** X, 'was found at index', L.index(i))
        break
else:
    print(2 ** X, 'not found')


# Task 4.c:
L = [1, 2, 4, 8, 16, 32, 64]
X = 5

if 2 ** X in L:
    print(2 ** X, 'was found at index', L.index(2 ** X))
else:
    print(2 ** X, 'not found')


# Task 4.d:	
X = 5
L = []
for i in range(7):
    L.append(2 ** i)

if 2 ** X in L:
    print(2 ** X, 'was found at index', L.index(2 ** X))
else:
    print(2 ** X, 'not found')


# Task 4.e:
L = []
for i in range(7):
    L.append(2 ** i)
X = 5
t = 2 ** X				# t is an fixed object - number

if t in L:
    print('at index', L.index(t))
else:
    print(X, 'not found')


# Task 4.f:
L = list(map(lambda x: 2 ** x, range(7)))
print(L)				# will return [1, 2, 4, 8, 16, 32, 64]





















