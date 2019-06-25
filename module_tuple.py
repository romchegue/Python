import os
l = []

for i in dir(os):
    if ord(i[0]) in range(97, 123):
        print(i)
        l = l + [i]

