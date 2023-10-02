# Задание №4
# 📌 Создайте декоратор с параметром.
# 📌 Параметр - целое число, количество запусков декорируемой
# функции.

from typing import Callable
from functools import wraps

def count(num: int = 1):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res_for_count = []
            result = None
            for _ in range(num):
                res_for_count.append(func(*args))
            return res_for_count
        return wrapper
    return deco


@count(2)
def sum_nums(a: int, b: int):
    sums = a + b
    return sums


print(sum_nums(22, 23))
print(sum_nums(12, 33))
print(sum_nums(12, 60))