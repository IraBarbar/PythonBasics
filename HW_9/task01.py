# 📌 Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
import math
import json
from typing import Callable
from pathlib import Path
import csv
import os
from functools import wraps
import random
from typing import Iterator
pp = Path(Path().cwd())


def gen_random_nums_csv():
    name = 'random_a_b_c.csv'

    """Генерируем случайные числа в файл:"""
    with open(pp/name, 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=['a', 'b', 'c'], dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        dict_row = {}
        for _ in range(random.randint(100, 1000)):
            dict_row['a'] = round(random.uniform(-100, 100), 2)
            dict_row['b'] = round(random.uniform(-100, 100), 2)
            dict_row['c'] = round(random.uniform(-100, 100), 2)
            csv_write.writerow(dict_row)

    """Считываем из файла:"""
    if os.path.exists(name):
        with open(pp/name, 'r', newline='') as f:
            csv_file: Iterator[dict] = csv.DictReader(f, fieldnames=['a', 'b', 'c'], dialect='excel-tab',
                                                      quoting=csv.QUOTE_NONNUMERIC)
            all_data = []
            for dict_row in csv_file:
                all_data.append(dict_row)
    else:
        all_data = []

    return all_data


def count(num: int = len(gen_random_nums_csv())):
    def decor(func: Callable):
        def wrapper(*args):

            """Вызываем функцию с данным из csv"""
            a, b, c = args
            lst_csv = gen_random_nums_csv()
            cache_dict = {}
            res_for_count = []
            for dict_ in lst_csv:
                a = dict_['a']
                b = dict_['b']
                c = dict_['c']
                cache_dict[str('a=' + str(a) + ', b=' + str(b) + ', c=' + str(c))] = func(a, b, c)
                res_for_count.append(func(a, b, c))

            """Сохраняем данные"""
            res = json.dumps(cache_dict, indent=2, sort_keys=True, ensure_ascii=False)
            with open(pp/'parametr.json', 'w', encoding='utf-8') as f:
                print(res, end='\n', file=f)

            return res_for_count
        return wrapper
    return decor

@count()
def square_leveling(a: float = 1, b: float = 1, c: float = 1) -> float:
    """Нахождение корней квадратного уравнения."""

    discr = b ** 2 - 4*a*c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2*a)
        x2 = (-b - math.sqrt(discr)) / (2*a)
        res = (round(x1, 2), round(x2, 2))
    elif discr == 0:
        x = -b / (2*a)
        res = round(x, 2)
    else:
        res = 'Корней нет'
    return res


for i in square_leveling(2,2,3):
    print(i)


