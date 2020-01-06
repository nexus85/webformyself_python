# def print_seconds_per_day(days=1):
#
#     h = 24 * days * 60 * 60
#     # m = h * 60
#     # s = m * 60
#     # print(s)
#     return h

#
# s = print_seconds_per_day(4) # вызов функции
# print(s)


def area_of_disk(radius):


    return radius * 3.14  ** 2

# print()
def area_of_ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)



#
#
# print(area_of_disk(34))
# print(area_of_ring(34,4))

# x = 10
# # y = 1
# # def fn(x):
# #     print(x)
# #     x = 20
# #     print(x)
# #     global y  #меняем значение глобальной переменной
# #     y = 10
# # fn(2)
# # print(x)
# # print(y)

# def fn(a, b=2, c=2):
#     pass
#
# fn(10, 20)


# print(1,2,3,4,5,5, sep="!!!")
# def fn(*params):
#     print(type(params)) # кортеж
#
#
# fn(3,3,23,2,5,2)


# def fn(**kwargs):
#     #сборка а словарь
#     '''
#
#
#     :param kwargs: Положител слова
#     :return: возвращается что то
#     '''
#     for p, m in kwargs.items():
#         print(p,m)
#
# fn(John=100, Mike=200, Pete=300)
#
# help(fn)

def fn():
    return 'Hello'