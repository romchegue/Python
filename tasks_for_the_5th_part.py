# Task 1.
'''
mymod.py - counts the number of lines and chars in the file.
'''

def countLines(name):
    '''
    countLines(name) - counts the number of lines in the file "name".
                       Example: countLines("/home/test_user1/test_dir1/test.txt")
    '''
    return len(open(name).readlines())

def countChars(name):
    '''
    countChars(name) - counts the number of chars in the file "name".
                       Example: countChars("/home/test_user1/test_dir1/test.txt")
    '''
    return len(open(name).read())

def countLines1(file):
    file.seek(0)
    return len(file.readlines())

def countChars1(file):
    file.seek(0)
    return sum(len(x) for x in file.read())

def test(name):
    if type(name) == str:
        return "File {0} contains: {1} lines; {2} chars.".format(name, countLines(name), countChars(name))
    else:
        return "File {0} contains: {1} lines; {2} chars.".format(name.name, countLines1(name), countChars1(name))

if __name__ == '__main__':
    print(test('mymod.py'))


# Task 2.
from mymod import test
test('test.txt')
from mymod import *
f = open('test.txt')
countChars('test.txt'); countLines('test.txt')
countChars1(f); countLines1(f)


# Task 3.
if __name__ == '__main__':
    print(test('mymod.py'))
	

# Task 4.
'''
myclient.py - imports mymod.py and check its operation.
'''
import mymod
text = 'test.txt'
file = open(text)

print(mymod.test(text), mymod.test(file))
print(mymod.countChars(text), mymod.countChars1(file))
print(mymod.countLines(text), mymod.countLines1(file))

------------------------------------------------------------------
'''
myclient1.py - imports mymod.py and check its operation.
'''
from mymod import test, countChars, countChars1, countLines, countLines1
text = 'test.txt'
file = open(text)

print(test(text), test(file))
print(countChars(text), countChars1(file))
print(countLines(text), countLines1(file))

------------------------------------------------------------------
def check_dict(module):
    for key in module.__dict__:
	    if not key.startswith('__'):
		    print(key)


# Task 5.
#/home/roma/PYTHON3
mkdir mypkg
vi ./mypkg/__init__.py
cp mymod.py ./mypkg/mymod1.py
import mypkg.mymod1
mypkg.TEST
'100000000000000000000000000000000000000000000'


# Task 6.
import myclient1
from imp import reload
reload(myclient1)


# Task 7.
# recur1.py
X = 1
import recur2
Y = 2

# recur2.py
from recur1 import X
from recur1 import Y

















