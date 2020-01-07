

def read_file(file):
    # try:
        with open(file, 'r', encoding='utf-8') as f:
            count = f.readline()
            list1 = []
            for i in f.readlines():
                list1.append(i.strip())
            if int(count)!= len(list1):
                raise Exception(f'Число строк больше заданного, в файле указанно {int(count)}, а в действительности {len(list1)}')
        return count, list1
    # except:
    #     print()

try:
    x, y = read_file('lab7')
except Exception as e:
    print(e)
except:
    print('Ошибка какая то')
else:
    print(f"Число строк заданно в файле {int(x)}, а размер файла {len(y)}")
    print(f'В файле: ', end=' ')
    for i in range(len(y)):
        print(y[i], sep=',', end=', ')





