def even_check():
    i = 0 
    max = int(input('Input max bound for even ckeck: '))
    while i < max:
        if max >= 100:
            print('Number {0} >= 100'.format(max))
            break
        if i % 2 != 0:
            print(i)
            i += 1
            continue
        else:
            print(i, ' is even number')
            i += 1
    else:
        print('Number {0} < 100'.format(max))
    return max
