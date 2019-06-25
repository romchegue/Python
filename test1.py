# Первый сценарий на языке Python
import sys # Загружает библиотечный модуль
print(sys.platform)
print(2 ** 100) # Возводит число 2 в степень 100
x = 'Spam!'
print(x * 8) # Дублирует строку
i = input('ENTER smth: ')
print('ord(' + i + ') = ' + str(ord(i)))
if ord(i) == 10:
    print('... ')
input('Press Enter for exit')
