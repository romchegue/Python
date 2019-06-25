def attr_list(OBJ):
    '''Argument: an object's link or an object. 
	   Ex.: 
	   attr_list('abcd') - string
	   attr_list(12345) - integer
	   attr_list([]) - list
	   attr_list(X) - variable
	
	'''
	
    L = dir(OBJ)                    #L is a list of valid attributes for that object
    c = 0                           #c is just counter
    while True:                     #We should repeat nested loop 'for i in L' because list L changes in this loop
        for i in L:
            if i[:2] == '__':       #Exclude inbuilt private methods such as: __class__, __repr__ and so on
                del L[L.index(i)]
                c += 1
        if c > 0:
            c = 0
        else: break
    return(L)

