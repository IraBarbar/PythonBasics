# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представлени

def dict_args(a=20, b='ser', c=(1, 2), d=str([1, 2]), t=str({'Python': 3.1}), h=25.2, l=5) -> dict:
    """Возвращающую словарь, где ключ — значение
    # переданного аргумента, а значение — имя аргумента."""

    dict_ = {}
    for key, val in locals().items():
        if isinstance(val, list | dict | frozenset | bytearray):
            dict_[(str(val))] = key
        else:
            dict_[val] = key
    dict_.popitem()
    return dict_


for i, j in dict_args().items():
    print(f'{str(i):<17}: {j}')

