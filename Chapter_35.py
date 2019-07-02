#####
try:
    try:
        raise IndexError
    finally:
        print('spam')
finally:
    print('SPAM')

#####
while 1:
    try:
        line = input()
    except EOFError:
        break

#####
try:
    input()
except Exception as E:
    print('caught', E.__class__)

#####
with open(r'/home/roma/Python/temp.txt', 'a') as myfile1, open('date.txt') as myfile2:
    for i in myfile2:
        myfile1.write('#' + i.upper())

#####
try:
    myfile1 = open(r'/home/roma/Python/temp.txt', 'a')
    myfile2 = open('date.txt')
    for i in myfile2:
        myfile1.write('##' + i.upper())
finally:
    myfile1.close()
    myfile2.close()

#####
def func(E = TypeError):  # Imitation of an outer program
    raise E

try:
    func(IndexError('SPAM'))
except:
    import sys
    print('uncought!', sys.exc_info()[0], sys.exc_info()[1], file=log)

#####
def func(E = TypeError(None)):  # Imitation of an outer program
    try:
        log = open('testlog.txt', 'a')
        raise E
    except:
        import sys, datetime
        print(str(datetime.datetime.now()), '- FAILED:', sys.exc_info()[0], sys.exc_info()[1], file=log)
    finally:
        log.close()

#####
import sys
log = open('testlog.txt', 'a')
from testapi import moreTests, runNextTest, testName   # ABSTRACTION!!!
def testdriver():
    while moreTests():
        try:
            runNextTest()
        except:
            print('FAILED', testName(), sys.exc_info()[:2], file=log)
        else:
            print('PASSED', testName(), file=log)

testdriver()

#####
def tester(func, *args):
    log = open('testlog.txt', 'a')
    try:
        func(*args)
    except Exception:
        import sys, datetime
        print("{date} - FAILED: {fnctn}({rgmnts}), ERROR: {cls} {exc}".format(date=str(datetime.datetime.now()), fnctn=func, rgmnts=args, cls=sys.exc_info()[0], exc=sys.exc_info()[1]), file=log)
    finally:
        log.close()


def errmaker(E = Exception()):
    raise E

tester(errmaker, ZeroDivisionError('SPAM'))

#####
mydictionary = {'spam': 10000}
while True:
    try:
        key = input('Input key: ')
        x = mydictionary[key]
    except KeyError:
        import sys
        print(sys.exc_info()[0:2])
        continue    
    else:
        print(x)
        break

#####











