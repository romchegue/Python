import time

t = time.time()
print(len(str(3 ** 2000000)))
print(str(round(time.time() - t, 2)) + ' s')