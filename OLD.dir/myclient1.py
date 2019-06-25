'''
myclient1.py - imports mymod.py and check its operation.
'''
from mymod import test, countChars, countChars1, countLines, countLines1
text = 'test.txt'
file = open(text)

print(test(text), test(file))
print(countChars(text), countChars1(file))
print(countLines(text), countLines1(file))

print('\nedited again version')

