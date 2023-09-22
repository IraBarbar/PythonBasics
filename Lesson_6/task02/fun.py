# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from random import randint as r
from sys import argv


def input_user_num(start: int, end: int):
    return int(input(f"Введите число от {start} до {end}:\n"))


def print_count(count_: int):
    return print(f'Осталось попыток: {count_}')


def print_more():
    return print('Больше')


def print_less():
    return print('Меньше')


def find_num(start: int, end: int, count_: int) -> bool:
    if start > end:
        start, end = end, start
    num_find = r(start, end + 1)
    while count_:
        num_user = input_user_num(start, end)
        if num_user == num_find:
            return True
        if num_user > num_find:
            end = num_user
            print_less()
        else:
            print_more()
            start = num_user
        count_ -= 1
        print('*' * 20)
        print_count(count_)
    return False
