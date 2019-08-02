# file: mytools.py

import time
def timer(label='', trace=True):    # Arguments of the decorator saves
    def onDecorator(func):          # At the stage of decoration
        def onCall(*args, **kwargs):  # When called: the original is called    
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            onCall.alltime += elapsed
            if trace:
                format = '{0} {1}: {2:.5f}, {3:.5f}'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format.format(*values))
            return result
        onCall.alltime = 0            # Assignment na attribute 'alltime' to the outer scope of the function
        return onCall
    return onDecorator

