
def test(file):
    with open(file, 'r') as f:
        f = f.readlines()
        return f

try:
    # f = test('fail')
    f = test('fiel')
except (EOFError, FileNotFoundError):
    print('Ошибка')
else:
    print(f)
finally:
    print('Работа заверщена')

