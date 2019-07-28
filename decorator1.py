# file: decorator1.py

class tracer:
    def __init__(self, func):   # at the stage of decoration @:
        self.calls = 0          # saves orginal function 'func'
        self.func = func
    def __call__(self, *args):  # On subsequent calls:
        self.calls += 1         # calls the oroginal function 'func'
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)

@tracer
def spam(a, b, c):    # spam = tracer(spam) - 'spam' is an instance of the class 'tracer' 
    print(a + b + c)  # Wraps the spam function with a decorator object
