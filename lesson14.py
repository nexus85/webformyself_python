# #
# # i = 1900
# # while i <= 2019:
# #     print(i)
# #     i +=1
# #
# #
#
# l = [1,2,3, 'hello', ['test', 10], 'world', True]
# print(type(l))
#
# l2 = list('hello')
# l3 = list((1,2,3))
# l4 = [i for i in 'hello']
# l5 = [i for i in 'hello World' if i != ' ' and i != 'e']
# l6 = [i for i in 'hello World' if i not in ['a','e','i','o','u']]
# l7 = list(range(0,10,3))
# print(l7)
# print(l4)
# print(l5)
# print(l6)
#
#
# print(l)
# print(l3)
# print(l2, sep='\n')


for i in range(1,3):
    print(f'Внешний цикл #{i}')
    for j in range(1,3):
        print(f'\tВнутрений цикл #{j}')