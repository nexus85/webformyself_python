# s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(type(s))
#
# print(s)
# s2 = set('hello')
# s3 = {i for i in range(1,11)}
# s4 = {1,3,4,5,1,3,4}
# print(s2)
# print(s3)
# print(s4)
#
#
# s4 = set()
# print(type(s4))
#
# nums = [1,2,3,4,1,1,2,3,5,5,3,3,4]
# nums2 = list(set(nums))
# print(nums)
# print(nums2)
#
#
# a = set

# a = set('abracadabre')
# b = set('alacazam')
# c = a - b#вычитнания
# d = a | b #объеденение
# e = a& b # перскния
# f =  a ^ b # множества из элиментов

# print(a,b,d,c, sep='\n')

s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
s2 = s.copy()
print(s, id(s))
print(s2, id(s2))