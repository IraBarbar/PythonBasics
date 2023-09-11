# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.
from pprint import pp


def dict_meen(*args, g=None) -> dict:
    """Возвращающую словарь, где ключ — значение
    # переданного аргумента, а значение — имя аргумента."""

    if g is None:
        g = globals()
    dict_ = {}
    for item in args:
        if isinstance(item, list | dict | frozenset | bytearray):
            dict_[(str(item))] = [n for n in g if id(g[n]) == id(item)]
        else:
            dict_[item] = [n for n in g if id(g[n]) == id(item)]
    return dict_


my_dict = (dict_meen(a := 20, b := 'ser', c := (1, 2), d := [1, 2], t := {'Python': 3.1}, h := 25.2, l := 5))
for key, val in my_dict.items():
    print(f'{str(key):>15}: {str(*val):>2}')
