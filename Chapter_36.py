# file: Chapter_36.py

def utf8_print(min=0, max=128, filename='/home/roma/Python/utf8simbols.txt'):
    # Maximum max value for UTF-8 is 1114112
    with open(filename, 'w') as output:
        print('(ord(i), chr(i))', file=output)
        for i in range(min, max):
            print('{0:>7} {1}'.format(i, repr(chr(i))), file=output)
    print("Results printed to", filename)


B = b'spam'
len(str(B, encoding='ascii'))

# file: domparse.py

from xml.dom.minidom import parse, Node
xmltree = parse('mybooks.xml')
print('\n', xmltree, '\n')
for node1 in xmltree.getElementsByTagName('title'):
    for node2 in node1.childNodes:
        if node2.nodeType == Node.TEXT_NODE:
            print(node2.data)


# file: saxparse.py
import xml.sax.handler
class BookHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.inTitle = False
    def startElement(self, name, attributes):
        if name == 'title':
            self.inTitle = True
    def characters(self, data):
        if self.inTitle:
            print(data)
    def endElement(self, name):
        if name == 'title':
            self.inTitle = False

import xml.sax
parser = xml.sax.make_parser()
handler = BookHandler()
parser.setContentHandler(handler)
parser.parse('mybooks.xml')


with open('D:\\roman\\Python\\temp.txt', mode='w', encoding='utf-8') as file:
    for i in range(0, 2001):
        line = "{0} ---> {1}\n".format(i, (chr(i), hex(i)))
        silent = file.write(line)







