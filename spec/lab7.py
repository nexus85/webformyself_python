

def read_file(file):

    with open(file, 'r', encoding='utf-8') as f:
        count = f.readline()
        list1 = []
        for i in f.readlines():
            list1.append(i.strip())
        # lines = f.readlines()
        # print(f)
        # print(count)
        # for i in range(int(count)):
        #     if i == 0:
        #         continue
        #     else:
        #         list1.append(f.readline, i)
        # print(lines)
    return count, list1

# def save_file():
#     pass
try:
    x, y = read_file('lab7')
except Exception as e:
    print(e)
except:
    print('Ошибка какая то')
else:
    print(x)
    print(y)





