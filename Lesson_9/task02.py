# Задание №2
# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами
# из диапазонов

from typing import Callable
import random
from functools import wraps


def decor(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        num, cnt, *_ = args
        if num not in range(1, 101):
            print('Загаданное число вне диапазона')
            num = random.randint(1, 100)
        if cnt not in range(1, 11):
            print('Количество попыток вне диапозона ')
            cnt = random.randint(1, 10)
        return func(num, cnt)

    return wrapper


@decor
def func_cnt(num: int, cnt: int):
    cnt_user = 0
    print(f'У вас {cnt} попыток')
    while cnt:
        cnt_user += 1
        num_user = int(input('Введите число:'))
        if num == num_user:
            return (f"Вы угодали число {num} за {cnt_user} попыток.")

        if num_user > num:
            print('Меньше')
        if num_user < num:
            print('Больше')
        cnt -= 1
    else:
        return (f'Вы не отгадали число {num} за {cnt_user} попыток.')


# func_cnt(2000, 20)