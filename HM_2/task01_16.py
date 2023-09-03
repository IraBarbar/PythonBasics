# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите число: '))
print(hex(num))
print('*' * 5)

div = 16
res = ''
flag = True

while flag:
    num16 = num//div
    remainder = num % div

    if remainder == 10:
        remainder = str('A')
    elif remainder == 11:
        remainder = 'B'
    elif remainder == 12:
        remainder = 'C'
    elif remainder == 13:
        remainder = 'D'
    elif remainder == 14:
        remainder = 'E'
    elif remainder == 15:
        remainder = 'F'
    res += str(remainder)

    if num16 < 16:
        remainder = num16
        if remainder == 10:
            remainder = str('A')
        elif remainder == 11:
            remainder = 'B'
        elif remainder == 12:
            remainder = 'C'
        elif remainder == 13:
            remainder = 'D'
        elif remainder == 14:
            remainder = 'E'
        elif remainder == 15:
            remainder = 'F'
        elif remainder == 0:
            remainder = ''
        res += str(remainder)
        flag = False
    num = num16
print(res[::-1])

