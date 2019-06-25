def fetcher(obj, index):
    print(obj[index])
    return obj[index]

def catcher():
    try:
        x = 100
        y = 200
        fetcher('hello', 7)
        z = 300
    except IndexError:
        print('got exception')
    print('continuing')

catcher()


try:
    raise IndexError
except IndexError:
    print('got exception')


raise IndexError('HELLO WORLD!')


assert False, 'Nobody expects the Spanish Inquisition!'


x = 'spam'
def after(a=4):
    try:
        fetcher(x, a)
    finally:
        print('after fetch')
    print('after try?')



def Try_Except_Finally(action, *args, error=Exception, exception=None, noexception=None, final=None):
    print("\n# Checking received arugments:\n# action = {0}\n# args = {1}\n# error = {2}\n# exception = {3}\n# noexception = {4}\n# final = {5}\n".format(action, args, error, 
	                                                                                            exception, noexception, final))
    try:
        action(*args)
    except error:
        print(exception)
    else:
        print(noexception)
    finally:
        print(final)
        input()


# ПРОВЕРКА:
def devis(x, y): 
    print(x / y)

Try_Except_Finally(devis, 10, 1, error=ZeroDivisionError, exception='EXCEPT...', elseexception='ELSE...', final='FINAL...')



raise ZeroDivisionError('\n' + ('~\v' * 5 + '\n') * 5)

try:
    100 / 0
except BaseException:
    print('BaseException .............................')
else:
    print('ELSE.......................................')
finally:
    print('\nHAPPY END!!!')


try:
    x = input()
    y = 1000 + int(x)
    print(y)
except (KeyboardInterrupt, ValueError):
    print('EXCEPTION (KeyboardInterrupt, ValueError)!!!')
except:
    print('EXCEPTION!!!')
finally:
    print('\nHAPPY END!!!')


import time
x = 1
while x:
    try:
        print('_' * x)
        x += 1
        time.sleep(1)
    except KeyboardInterrupt:
        f = input('\nDO YOU REALLY WANT TO QUIT? (y/...')
        if f.lower()[:1] == 'y':
            print('\nGOOD BYE!!!\n')
            x = 0


 


   
    
 