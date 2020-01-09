import re

file = open('lab8', 'r').read()
file = file.split("\n")

r1 = '\d{2}:\d{2}:\d{2}'
r2 = '\d{3}'
r3 = '\w* [А-Я]{1}\w*'


for x in file:
    if (re.findall(r3, x)):
        t = (re.search(r1, x))
        n = (re.search(r2, x))
        c = (re.search(r3,x))
        print(t.group(0) + " - Поезд No " + n.group(0) + " " + c.group(0))

