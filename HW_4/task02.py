# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.
from pprint import pp


def dict_args(a=20, b='ser', c=(1, 2), d=str([1, 2]), t=str({'Python': 3.1}), h=25.2, l=5) -> dict:
    """Возвращающую словарь, где ключ — значение
    # переданного аргумента, а значение — имя аргумента."""

    dict_ = {}
    for key, val in locals().items():
        if isinstance(val, list | dict | frozenset | bytearray):
            dict_[(str(val))] = key

        else:
            dict_[val] = key
    return dict_


my_dict = dict_args()
for i, j in my_dict.items():
    print(f'{str(i):<95}: {j}')

