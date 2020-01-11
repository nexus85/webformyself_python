# # def sum_of(start, end, fn):
# # #     n = 0
# # #     for i in range(start, end+1):
# # #         n += fn(i)
# # #     return n
# # #
# # # def ints(x): return x
# # # def squares(x): return x ** 2
# # #
# # #
# # # print(sum_of(1,10, ints))
# # # print(sum_of(1,10, squares))
# # # print(sum_of(1,10, lambda x: x ** 2)) #анонимная функция
#
# lst = [1,2,3,4,5,6,6]
# new_lst = []
# for item in lst:
#     new_lst.append(str(item))
#
# new_lst2 = list(map(str, lst))
# print(lst)
# print(new_lst)
# print(new_lst2)
#
# new_lst3 = list(map(lambda i: i* 10, lst))
# print(new_lst3)
#
# lst = [6, 3,7,2,6,9,4,8]
#
# # new = list(map())
# new_lst4 = set(filter(lambda i: i > 5, lst))
# print(new_lst4)
#
#
# from functools import reduce
# lst = [1,2,3,4,5]
# print(sum(lst))
#
# sum_all = reduce(lambda a,b: a + b, lst) # передает сумма, т.е. а + б, потом берет третье значение и прибовляет сумму полученное при п
# # первом вычислении
# print(sum_all) #15
#
# lst = [0,9,3,4,5]
# # lst = [1,2,3,4,5]
# sum_all = reduce(lambda a,b: a if(a>b) else b, lst)  #9
# # sum_all = reduce(lambda a,b: a + b, lst, 100)
# print(sum_all)
#
#
# a = [1,2,3]
# b = 'xyz'
# c = (None, True, False, 1)
# z = list(zip(a,b,c))  # [(1, 'x', None), (2, 'y', True), (3, 'z', False)]  #рабоатет по наименьшей
# print(z)  # возвращается котежи
#
#
from functools import reduce

#
# lst = [6,3,7,2,6,9,4,8]
# lst = list(filter(lambda i: i>5, lst))
# lst = list(map(lambda i: i*10, lst))
# sum_all = reduce(lambda a,b: a+b, lst)
#


# def compose(f, g):
#     return lambda x: f(g(x))

# def double(x): return x*2
# double = lambda x: x*2
#
# inc = lambda x: x + 1
#
# # inc_and_double = compose(double, inc)
# inc_and_double = lambda x: double(inc(x))
# d = inc_and_double(4)
# print(d)
#
#
# def add(x):
#     return lambda y: x + y
# a = add(10) #
# print(a(2))
# print(a(6))\
#
#     #способность функции сохрянять ссылку на перменнною объявленную вне его контекта
#
# def add1(x):
#     def ret(y):
#         return y + x
#     return ret
#
#
# a = add1(10)
# print(a(40))


# def setup(lst):
#     i=0
#     def ret():
#         nonlocal i
#         v = lst[i]
#         i+= 1
#         return v
#     return ret
#
# next_val = setup([1,2,3,4,5])
# print(next_val())
# print(next_val())
# print(next_val())
# print(next_val())


# def hello():
# #     return 'hello'
# #
# # def add_undes(fn):
# #     return lambda name:'_' + fn(name) + '_'
# #
# # @add_undes # тоже самое что # hello = add_undes(hello)
# # def hello(name):
# #     return 'hello', + name
# # # hello = add_undes(hello)
# # # print(hello)
# # # print(hello())

def add_u(understroke):
    def decor(fn):
        def wrapper(name):
            return '_' + fn(name) + '_'
        return wrapper()
    return decor()
@add_u('==============')
def hello(name):
    return 'Привет' + name

hello('Вася')