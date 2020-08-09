# file: tracer.py

def Tracer(aClass):                         # At the stage of decoration @:
    class Wrapper:
        def __init__(self, *args, **kwargs):        # At the stage of creation of an instance 
            self.fetches = 0
            self.wrapped = aClass(*args, **kwargs)
        def __getattr__(self, attrname):
            print('Trace: ' + attrname)
            self.fetches += 1
            return getattr(self.wrapped, attrname)
    return Wrapper
