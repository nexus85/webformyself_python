# r = range(10)
#
# print(r)
# print(type(r))

# for i in range(1, 11):
#     print(i)
#


# l = [1,2,4,5,3,2]
# print(l)
#
# for i in l:
#     print(i)
# l.append(6) # добавить в список, в конец.
# print(l)
# print(l[2])
# l[2] = 22
# print(l[2])

#
# r = range(6)
# print(r[3])
#
# help(range)


#Строку изменить нельзя
# print(list("abc"))


# l = [32,345,345,34,534,536,467,56,74]
# l.append('3')
# d = l.pop()
# a = l.pop(0)
# s = l.sort()
#
#
# print(l)
# print(d)
# print(a)
# print(s)
# print(l)


# t = (1,2,3) #кортеж, не изменяемый
# print(type(t))
# a = 1
# b = 2
# print(a,b)
# a,b = b,a
# print(a,b)

# l = [1,2,3,]
# l3 = l
#
#
# l2 = l.copy()
#
# print(l, l3)
# print(id(l),id(l3))
# print(id(l), id(l2))
#
# l3[1] = 3
# l2[1] = 4
# print(l, l3,l2)
# # print(id(l),id(l3),id(l2))
#
#
# #словарь
#
# d = {'a': 100, 'b':200, 'c': 300}
# print(d['a'])
# print('y' in d)
# print('a' in d)
#
# print(d.get('a',0))
# print(d.get('x',0)) # если нет, то вернется второе значение, если есть, то вернетчся значение.
#
# for k, v in d.items():
#     print(k,v)
#
# print(d.values()) #вывести все значения
# print(d.keys()) #вывети все ключи
#
#
# #Срезы
# l = [214,35,34,534,5,25,1,45,234,5342,52]
# print(l[5:])
# print(l[:5])
# print(l)
# print(l[::-1])
# print(30 not in l)
# print(30 in l)
# # получить копию
# l2 = l[:]
# print(id(l), id(l2))
#
#
# i = list(d for d in range(1,10))
# print(i)

# l = []
# for i in [2,3,4]:
#     l.append(i**2)
# print(l)
#
# k = list(d ** 2 for d in [2,3,4])
# print(k)

# проверка значения
hello = {
    'ru': 'Добрый день',
    'en': 'Good day',
    'de': 'Guten tag',
    'dk': 'God dag',
    'default': 'Unknow language'
}
s = input('Введите код: ')
greet = hello.get(s, hello['default'])
print(greet)

