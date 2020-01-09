import re

# s = 'Python Programming. for the Absolute. Beginner'
# # r = re.findall(r'.', s)
# r = re.findall(r'\.', s)
# r = re.findall(r'\w', s) #без пробелов
# r = re.findall(r'[for]', s) # только символы f o r
# r = re.findall(r'[^for]', s) # любые но не символы f o r
# r = re.findall(r'[a-zA-Z0-9]', s) # любые но не символы f o r
# r = re.findall(r'\w', s) #[a-zA-Z0-9]
# r = re.findall(r'\w{3}', s) #[a-zA-Z0-9] по три букывы
# r = re.findall(r'\w{3} ', s) #[a-zA-Z0-9] три буквы пробел
# r = re.findall(r'\w$', s) #[a-zA-Z0-9] пследняя буква
#
#
#
# print(r)
s = 'Python Programming. for the Absolute. Beginner'
s = 'abc.test@gmail.com'
r = re.findall(r'@\w+.\w+',s)

s1 = 'abc 12-1234 12-02-2017, asd 56-1235 1-05-2016, xyz 78-1235 25-1-2018'
# r1 = re.findall(r'\d{1,2}-\d\d?-\d{4}', s1)
r1 = re.findall(r'\d{1,2}-\d\d?-(\d{4})', s1)   #групировка, то в круглых скобках то и попадает в регулярку

print(r1)
# {0,} => *
# {1,} => +
# {0,1} => ?
# [0-9]  => \d
# [^0-9]  => \D

#[a-zA-Z0-9]   ===> \w
#[^a-zA-Z0-9]   ====> \W




print(r)