# Задание №3
# 📌 Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# 📌 Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# 📌 Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# 📌 Имя файла должно совпадать с именем декорируемой
# функции.
from typing import Callable
from pathlib import Path
import json
import os
from functools import wraps
pp = Path(Path().cwd())


def decor(func: Callable):
    """Cохраняет в json файл параметры декорируемой функции и результат."""
    _cache_dict = {}

    @wraps(func)
    def wrapper(*args):
        name = func.__name__ + '.json'

        """Читаем файл"""
        if os.path.exists(name):
            with open(pp/name, 'r', encoding='UTF-8') as file:
                data = json.load(file)
        else:
            data = {}
        _cache_dict = data

        if args not in _cache_dict:
            _cache_dict[str(args)] = func(*args)

        """Записываем файл"""
        res = json.dumps(_cache_dict, indent=2, sort_keys=True, ensure_ascii=False)
        with open(pp/name, 'w', encoding='utf-8') as f:
            print(res, end='\n', file=f)
        return _cache_dict[str(args)]

    return wrapper


@decor
def sum_nums(a: int, b: int):
    sums = a + b
    return sums


# print(sum_nums(22, 23))
# print(sum_nums(12, 33))
# print(sum_nums(12, 60))

