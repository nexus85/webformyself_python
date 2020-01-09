import re

regexp = 'a'
# regexp = 'a'
s = "vasyA@mail.ru"


# m = re.match(regexp, s)
m = re.search(regexp, s, re.I) # re.I игнорировать регистр
print(m.group(0), m.start(), m.end())

print(s.find('a')) #использование метода для поиска

#поиск всех букв а

m2 = re.findall(regexp,s)
print(m2)

split1 = re.split('-', '10-443-34-34-34-34')
split2 = re.split('-', '10-443-34-34-34-34', maxsplit=2) #maxsplit=2 только два разьет
print(split1,'\n', split2)

# re.match()
# re.search()
# re.findall()
# re.split()
# sub = re.subn('a', 'b', s) #ищет вхождение a и меняет их b
sub = re.subn('a', 'b', s) #ищет вхождение a и меняет их b
print(sub)

