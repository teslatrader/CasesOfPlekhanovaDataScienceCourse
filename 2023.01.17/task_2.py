# Задача 2.
# Решите уравнение 𝑎𝑥 ± 𝑏 = 0.
# Вводится строка в формате
# 𝑎𝑥 + 𝑏 = 0 или 𝑎𝑥 − 𝑏 = 0,
# где вместо 𝑎 — целое число,
# вместо 𝑏 — целое неотрицательное число.
# Числа по модулю не превосходят 1000.
# Число 𝑎 может быть пропущено, если оно равно 1. 𝑏 всегда присутствует, 𝑥 также всегда присутствует, даже если а = 0.
# Выведите корни уравнения, если их конечное число; 'NO', если корней нет и 'INF', если корней бесконечно много.

from sys import exit

equation = input("Введите уравнение типа: ax +/- b = 0.\n")
equation = equation.replace(' ', '')
equation = equation.replace('=0', '')
a = 0
b = 0

if len(equation) == 1:
    b = int(equation[0])
    if b == 0:
        print(f'We have INF number of roots: b is {b}')
    else:
        print(f'We have INVALID equation. b is {b}. NO roots: b != 0')
elif len(equation) == 0:
    print('We have invalid equation input.')
else:
    is_plus = equation.find('+') > 0

    if is_plus:
        axb = equation.split('+')
    else:
        axb = equation.split('-')

    if len(axb) != 2:
        print('Check the equation input. Something is wrong.')
    else:
        ax = axb[0].split('x')

        if ax[0] == '':
            a = 1
            if not equation[-1].isdigit():
                b = equation[-1]
                print(f'A and B were defined incorrectly: a = {a}, b = {b}')
            else:
                b = int(equation[-1])
        else:
            if not equation[0].isdigit() or not equation[-1].isdigit():
                a = equation[0]
                b = equation[-1]
                print(f'A and B were defined incorrectly: a = {a}, b = {b}')
            else:
                a = int(ax[0])
                b = int(axb[-1])
        print(f'a = {a}, b = {b}')

        if abs(a) > 1000 or abs(b) > 1000:
            print(f'A or B is more than allowed limit = 1000. Check input equation.')
        else:
            if is_plus:
                x = round(-b / a, 3)
            else:
                x = round(b / a, 3)
            print(f'x is {x}')
