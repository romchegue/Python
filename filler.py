# file: filler.py

def filler(collection={}):
    '''
    This function will help you to create and quickly fill a dictionary.
    If you pass in argument your existing dictionary the function will 
	fill it with a copy.
	'''
    collection = collection.copy()
    print('Press Ctrl+C to stop filling')
    try:
        while True:
            attr_value = input('ATTR=VALUE: ')
            attr_value = attr_value.replace(' ', '').split('=')
            collection[attr_value[0]] = attr_value[1]
    except KeyboardInterrupt:
        print('...\nThe end')
    return collection
