'I am: docstr.__doc__'

def func(args):
    'I am: docstr.func.__doc__'
    pass

class spam:
    'I am: spam.__doc__ or docstr.spam.__doc__'
    def method(self, arg=None):
        'I am: spam.method.__doc__ or self.method.__doc__'
        self.arg = arg
    attr = 'SPAM'

