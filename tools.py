# file: tools.py

def safe(func, *args):
    try:
        func(*args)
    except:
        import sys
        print(sys.exc_info())

