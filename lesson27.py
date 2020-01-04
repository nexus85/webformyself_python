



# def set_register(str):
#     if ' ' in str:
#         return str.upper()
#     else:
#         return str.lower()
#
#
# s = 'Hello World'
#
# print(set_register(s))

#
# def get_sum(a,b,c,d):
#     return a + b + c + d
# print(get_sum(1,2,5,7))


# def get_sum(*args):
#     return sum(args)
#
# print(get_sum(1,2,4))


# def func(**kwargs):
#     print(kwargs)
#
# print(func(a=2, b=5, c=20))

# def f(a,x, *args, **kwargs):
#     print(a)
#     print(x)
#     print(args)
#     print(kwargs)
#
# s = f(1,2,3,4,b='test', c='hi')
# print(s)



l = [1,2,3]
def f2(l):
    def get_mult(x):
        return x * 2
    return [get_mult(i) for i in l]



print(f2(l))

"""
homeWork

"""