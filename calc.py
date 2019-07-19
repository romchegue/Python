# file: calc.py

def calc():
    hint = '''
'?' - help
'*' - multiplication. Ex.: x * y
'/' - division. Ex.: x / y
'+' - addition. Ex.: x + y
'-' - subtraction. Ex.: x - y
'**' - exponentiation. Ex.: x ** y
'()' - prioritization. Ex.: (x + y) * z
'%' - remainder of division. Ex.: x % y
'//' - obtaining the integer part of the division. Ex.: x // y
'abs()' - number modulus. Ex.: abs(x)
'-x' - the change of the sign of the number. Ex.: -x
'divmod(x, y)' - a couple (x // y, x % y). Ex.: divmod(x, y)
'pow(x, y[,z])' - x^y modulo (if the module is specified). Ex.: pow(x, y, z)
'''
    while True:
        try:
            x = input("Expression or '?' for help: ")
            if '?' in x:    # Calls help hint
                print(hint)
                continue
            else:
                res = eval(x)   # Dangerous operation!!!
        except SyntaxError as E:    # Errors of an input
            print('SyntaxError:', E)
            continue
        if type(res) not in [float, int, complex]:   # check the type
            print('TypeError:', res)
            continue
        else:
            print(res)

