form = [9, 15, 19, 23, 25, 27, 29, 29, 31, 31, 31, 31, 29, 29, 27, 25, 23, 19, 15, 9]
for i in form:
    s = '{0:^50}'.format('_' * i)
    print(s) 

	
#######################################

def circle(x='#'):
    form = [9, 15, 19, 23, 25, 27, 29, 29, 31, 31, 31, 31, 29, 29, 27, 25, 23, 19, 15, 9]
    ListCircle = []
    for i in form:
        s = '{0:^50}'.format(x * i)
        ListCircle = ListCircle + [s]
    return ListCircle	
