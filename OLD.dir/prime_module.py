def prime(y):
    x = y // 2
    while x > 1:
        if y % x == 0: 
            print(y, 'has factor', x)
            break
        x = x-1
    else: 
        print(y, 'is prime')
    
prime(13)
prime(13.0)
prime(15)
prime(15.0)

######################################

def prime_new(y):
    x = y // 2
    for x in range(x, 1, -1):
         if y % x == 0: 
            print(y, 'has factor', x)
            break
    else: 
        print(y, 'is prime')

prime(13)
prime(13.0)
prime(15)
prime(15.0)

