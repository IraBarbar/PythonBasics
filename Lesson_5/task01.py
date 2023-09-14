# Задание №1
# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
# хранятся в кортеже как значения второго ключа.
from typing import Dict, Tuple

def input_user() -> str:
    return input('Введите строку из четырёх или более целых чисел, разделённых символом “/”.')

def dict_nums() -> dict:
    """ Словарь с цифрами от пользователя."""

    num1, num2, num3, *num = input_user()\
        .replace(' ', '') \
        .split('/')
    new_dict: dict[int, int | tuple[int, ...]] = {int(num2): int(num1), int(num3): tuple(map(int, num))}
    return new_dict


for key, val in dict_nums().items():
    print(f'{key}: {val}')

    