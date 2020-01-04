l = [1,2,3,'hello',['test',10], 'world', True]
name = ['Ivanov', 'Petrov', 'Sidorov']



print(len(l))
# print(len(l))
l[2] = 'World'
# l[:2] = [10,15]
l.append('Hello')
l.extend(name)

l2 = ['hi',19]
l += l2
l.insert(4,name)
l.remove(True)
el = l.pop()
el2 = l.pop(2)
print(el)
print(el2)
l.append('test')
count = l.count('test')
# l.sort()
# print(count)


l3 = ['hello', 'hi', 'Devid', 'World', 'test', 'Ann']
print(l3)
print(l3, l3.sort())
print(l)

