import re

regexp = 'v'
# regexp = 'a'
s = "vasya@mail.ru"


m = re.match(regexp, s)
print(m.group(0))