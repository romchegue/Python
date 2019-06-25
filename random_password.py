def passwd(len=10):
    P = ''
    import random
    for i in range(len):
        P += chr(random.randint(32, 127))
    return(P)
