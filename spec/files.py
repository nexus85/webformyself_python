
# работа с файлами
# f = open('test.txt', 'r', encoding='utf-8') # r - на чтение, r+ и на чтение и на запись, w - на запись, w+ и на запись и на чтение
# # .. r+ w+(все уничтожается при записе, хорошо подходит для перезапись
# # a и a+ - когда файл открыаетя, то курсор стоит в конце, хорош для дозаписи
# #encoding - кодировка файла
#
#
#
# f.close() # закрытие файла.


# with open('test.txt', 'a', encoding='utf-8') as f:    # способ лучший чем выше приведеный
    # print(f.read(5))
    # print(f.read(2))
    # print(f.read())
    # s = f.readline() #читает строку
    # while s:
    #     print(s)
    #     s = f.readline()
    # lines = f.readlines() #читает все строки
    # print(lines)
    # for line in f:
    #     print(line)
    # for line in lines:
    #     print(line)

    # f.write('\nline 6')
    # for i in range(99):
#     #     f.write(f'line {i+1} \n')
#
#
#     print(f.closed)
#     print(f.mode)
#     print(f.name)


# import csv
# with open('data.csv', 'a', newline='\n') as f:
#     # reader = csv.reader(f, delimiter=',')  #delimitor - разделитель
#     writer = csv.writer(f, delimiter=',')  #delimitor - разделитель
#     writer.writerow(['pite', 'Harrison',21, '434-32-44'])
#     # for row in reader:
#     #     print(row)


import os
# print(os.getcwd())
# print(os.path.exists('data.csv'))
# print(os.path.exists('data1.csv'))
# print(os.listdir())
# print(os.listdir('/'))
# print(dir(os))
# # os.rename('demo1.py','d.py')
# print(os.path.getmtime('test.txt'))