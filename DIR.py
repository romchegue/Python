

def DIR(L):      #L is dir()
    D = {}
    for i in L:
        if i[:2] != '__':
            D[i] = str(eval(i))
    return(D)

for i in DIR(L):
    print(i + '\t--->\t' + DIR(L)[i])

input()
