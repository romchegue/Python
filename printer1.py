#!/usr/bin/python36
s = str(input('Input a set of characters: ')) * 100

while True:         # helps to avoid errors of input a width of an output
    try:
        w = int(input('Input a width of the output: '))
        break  
    except:
        pass

t = 0               
for i in s:         # prints string s in a format with width w 
    print(i, end='')
    t += 1
    if t % w == 0:
        print('')