'''
myclient.py - imports mymod.py and check its operation.
'''
import mymod
text = 'test.txt'
file = open(text)

print(mymod.test(text), mymod.test(file))
print(mymod.countChars(text), mymod.countChars1(file))
print(mymod.countLines(text), mymod.countLines1(file))

