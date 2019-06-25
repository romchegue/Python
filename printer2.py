#!
ur = int(input('Input an upper bound of range: '))
s = ''
for i in range(ur):
    s = s + str(i)

w = 1       # a width of output
t = 1       # an iterator
          
for i in s:         
    print(i, end='')
    if t == w:       # presses an Enter width += 1
        print('')
        w = w + 1
        t = 0
    t += 1
    
    
