# d = {}
# product1 = {'title': 'Sony', 'price': 100}
# print(product1)
# print(product1['title'])
#
# product2 = dict(title="Iphone", price=110)
#
# users = [
#     ['bob@gmail.com', 'Bob'],
#     ['katy@gmail.com', 'Katy'],
#     ['john@gmail.com', 'John']
# ]
# d_users = dict(users)
# print(d_users, type(d_users))
#
#
# print(type(d))


product1 = {'title': 'Sony', 'price': 100}
prod = dict.fromkeys(['price', 'price2'])
print(prod)

nums = {i: i + 1 for i in range(1,10)}
print(nums)

for key in product1:
    print(f'{key}: {product1[key]}')

for key, value in product1.items():
    print(key)
    print(value, end="!", sep='R')

products = [
    {'title':'Sony','price':100},
    {'title':'Sony','price':100},
    {'title':'Sony','price':100},
]

print(products)
for product in products:
    print(product['title'], product['price'])