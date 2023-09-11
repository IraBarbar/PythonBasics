# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.
from pprint import pp


def dict_symbol_meaning(str_: str):
    """Возвращает словарь ключ chr(integer) значение  integer."""

    new_dict = {}
    new_list = str_.split()
    if int(new_list[0]) > int(new_list[1]):
        start = int(new_list[1])
        end = int(int(new_list[0]))
    else:
        start = int(new_list[0])
        end = int(int(new_list[1]))
    for i in range(start, end + 1):
        new_dict.setdefault(chr(i), i)
    return sorted(new_dict.items(), key=lambda item: item[1])


my_str = '110 30'
pp(dict_symbol_meaning(my_str))
