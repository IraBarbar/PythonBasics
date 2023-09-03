# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions
from decimal import Decimal

a, b, c, d = 2, 50, 0, -75550

list_common_divisors_numerator = []
list_common_divisors_denominator = []
common_divisor = 1

if b == 0 or d == 0:
    print('Ошибка! Знаменатель не может быть 0.')

else:

    f1 = fractions.Fraction(a, b)
    print(f1)
    f2 = fractions.Fraction(c, d)
    print(f2)
    print(f1 + f2, '- сумма дробей')
    print(f1 * f2, '- произведение* дробей')
    print('*' * 10)

    if abs(a) < abs(b):
        min_num = abs(a)
    else:
        min_num = abs(b)
    for i in range(2, min_num + 1):
        if a % i == 0:
            list_common_divisors_numerator.append(i)

        if b % i == 0:
            list_common_divisors_denominator.append(i)

    if list_common_divisors_numerator and list_common_divisors_denominator:
        for i in range(len(list_common_divisors_numerator)):
            for j in range(len(list_common_divisors_denominator)):
                if list_common_divisors_numerator[i] == list_common_divisors_denominator[j] > common_divisor:
                    common_divisor = list_common_divisors_numerator[i]

    a = int(a / common_divisor)
    b = int(b / common_divisor)

    if ((a < 0) and (b > 0)) or ((a > 0) and (b > 0)):
        print(f'{a}/{b}' if b != 1 else f'{a}')
    elif (a > 0) and (b < 0):
        print(f'-{a}/{abs(b)}' if b != 1 else f'{a}')
    elif (a < 0) and (b < 0):
        print(f'{abs(a)}/{abs(b)}' if b != 1 else f'{a}')
    elif a == 0:
        print(a)

    list_common_divisors_numerator = []
    list_common_divisors_denominator = []
    common_divisor = 1

    if abs(c) < abs(d):
        min_num = abs(c)
    else:
        min_num = abs(d)
    for i in range(2, min_num + 1):
        if c % i == 0:
            list_common_divisors_numerator.append(i)

        if d % i == 0:
            list_common_divisors_denominator.append(i)

    if list_common_divisors_numerator and list_common_divisors_denominator:
        for i in range(len(list_common_divisors_numerator)):
            for j in range(len(list_common_divisors_denominator)):
                if list_common_divisors_numerator[i] == list_common_divisors_denominator[j] > common_divisor:
                    common_divisor = list_common_divisors_numerator[i]

    c = int(c / common_divisor)
    d = int(d / common_divisor)

    if ((c < 0) and (d > 0)) or ((c > 0) and (d > 0)):
        print(f'{c}/{d}' if d != 1 else f'{c}')
    elif (c > 0) and (d < 0):
        print(f'-{c}/{abs(d)}' if d != 1 else f'{c}')
    elif (c < 0) and (d < 0):
        print(f'{abs(c)}/{abs(d)}' if d != 1 else f'{c}')
    elif c == 0:
        print(c)

    # Сложение:

    if b == d:
        x1 = a + c
        x2 = b
    else:
        x1 = a * d
        x3 = c * b

        x2, x4 = b * d, b * d

        x1 = x1 + x3

    list_common_divisors_numerator = []
    list_common_divisors_denominator = []
    common_divisor = 1

    if abs(x1) < abs(x2):
        min_num = abs(x1)
    else:
        min_num = abs(x2)
    for i in range(2, min_num + 1):
        if x1 % i == 0:
            list_common_divisors_numerator.append(i)

        if x2 % i == 0:
            list_common_divisors_denominator.append(i)

    if list_common_divisors_numerator and list_common_divisors_denominator:
        for i in range(len(list_common_divisors_numerator)):
            for j in range(len(list_common_divisors_denominator)):
                if list_common_divisors_numerator[i] == list_common_divisors_denominator[j] > common_divisor:
                    common_divisor = list_common_divisors_numerator[i]

    x1 = int(x1 / common_divisor)
    x2 = int(x2 / common_divisor)

    if ((x1 < 0) and (x2 > 0)) or ((x1 > 0) and (x2 > 0)):
        print(f'{x1}/{x2}' if x2 != 1 else f'{x1}', '- сумма дробей')
    elif (x1 > 0) and (x2 < 0):
        print(f'-{x1}/{abs(x2)}' if x2 != 1 else f'{x1}', '- сумма дробей')
    elif (x1 < 0) and (x2 < 0):
        print(f'{abs(x1)}/{abs(x2)}' if x2 != 1 else f'{x1}', '- сумма дробей')

    # произведение* дробей:

    a = a * c
    b = b * d

    list_common_divisors_numerator = []
    list_common_divisors_denominator = []
    common_divisor = 1

    if abs(a) < abs(b):
        min_num = a
    else:
        min_num = b
    for i in range(2, min_num + 1):
        if a % i == 0:
            list_common_divisors_numerator.append(i)

        if b % i == 0:
            list_common_divisors_denominator.append(i)

    if list_common_divisors_numerator and list_common_divisors_denominator:
        for i in range(len(list_common_divisors_numerator)):
            for j in range(len(list_common_divisors_denominator)):
                if list_common_divisors_numerator[i] == list_common_divisors_denominator[j] > common_divisor:
                    common_divisor = list_common_divisors_numerator[i]

    a = int(a / common_divisor)
    b = int(b / common_divisor)

    if ((a < 0) and (b > 0)) or ((a > 0) and (b > 0)):
        print(f'{a}/{b}' if b != 1 else f'{a}', '- произведение* дробей')
    elif (a > 0) and (b < 0):
        print(f'-({a}/{abs(b)})' if b != 1 else f'{a}', '- произведение* дробей')
    elif (a < 0) and (b < 0):
        print(f'{abs(a)}/{abs(b)}' if b != 1 else f'{a}', '- произведение* дробей')
    elif a == 0:
        print(f'{a}', '- произведение* дробей' )
