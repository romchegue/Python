# file patternparse.py

import re
text = open('mybooks.xml').read()
found = re.findall('<title>(.*)</title>', text)
print(found, '\n')
for title in found: print(title)
