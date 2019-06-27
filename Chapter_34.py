# file: Chapter_34.py

def exceptor():
    x = input('INPUT SMTH: ')
    try:
        print(eval(x))
    except Exception:
        import sys
        return sys.exc_info()       # Get the last instance of an exception 


def exceptor1():
    x = input('INPUT SMTH: ')
    try:
        print(eval(x))
    except Exception as X:                        # X - a raised instance
        return (X.__class__, X, X.__traceback__)  # The same as sys.exc_info()

