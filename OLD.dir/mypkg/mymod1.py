'''
mymod.py - counts the number of lines and chars in the file.

'''

def countLines(name):
    '''
    countLines(name) - counts the number of lines in the file "name".
                       Example: countLines("/home/test_user1/test_dir1/test.txt")

    '''
    file = open(name)
    return len(file.readlines())


def countChars(name):
    '''
    countChars(name) - counts the number of chars in the file "name".
                       Example: countChars("/home/test_user1/test_dir1/test.txt")

    '''
    file = open(name)
    return sum(len(x) for x in file.read())


def countLines1(file):
    file.seek(0)
    return len(file.readlines())


def countChars1(file):
    file.seek(0)
    return sum(len(x) for x in file.read())


def test(name):
    if type(name) == str:
        return "File {0} contains: {1} lines; {2} chars.".format(name, countLines(name), countChars(name))
    else:
        return "File {0} contains: {1} lines; {2} chars.".format(name.name, countLines1(name), countChars1(name))


if __name__ == '__main__':
    print(test('mymod.py'))

