num = 4
humanC = 0
c = 0
while humanC != num:
        humanC = int(input("введите число: "))
        c += 1
        if humanC > num:
            print(f'Ваше число больше. Вы загадали {humanC}')
        elif humanC < num:
            print(f'Ваше число меньше. Вы загадали {humanC}')
print(f'Вы угодали {humanC}, число попыток {c}')