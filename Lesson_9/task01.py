# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from typing import Callable
import random


def func_num():
    num: int = random.randint(1, 100)
    cnt: int = random.randint(1, 10)

    def func_cnt():
        nonlocal num, cnt
        cnt_user = 0
        print(f'У вас {cnt} попыток')
        while cnt:
            cnt_user += 1
            num_user = int(input('Введите число:'))
            if num == num_user:
                print(f"Вы угодали число {num} за {cnt_user} попыток.")
                break
            if num_user > num:
                 print('Меньше')
            if num_user < num:
                print('Больше')
            cnt -= 1
        else:
            print(f'Вы не отгадали число {num} за {cnt_user} попыток.')
        
    return func_cnt


primer = func_num()
primer()