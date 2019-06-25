D = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'H'}
D['10'] = D
t = 0
s = "D['10']"

while eval(s) == D:
    print(eval(s))
    s = s + "['10']"
    t += 1
    if t >= 50:
        print('t >= 50')
        print('s = ' + str(s))
        break

