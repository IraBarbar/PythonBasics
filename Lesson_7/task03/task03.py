# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.
from pathlib import Path
import os
import itertools

os.chdir('..')
p = Path(Path().cwd())


def read_name_data(dir_name: str, file_name: str) -> list:
    """Считываем данные построчно в список."""

    with(
     open(p/f'{dir_name}' / f'{file_name}', 'r', encoding='utf-8') as f

    ):
        lst = []
        while res := f.readline():
            lst.append(res)
    return lst


def lst_new_file(f_name, f_data) -> list:

    # Сравниваем длинну и увеличиваем короткую:
    if len(f_data) > len(f_name):
        len_max = len(f_data)
        f_name = list(itertools.islice(itertools.cycle(f_name), len_max))
    else:
        len_max = len(f_name)
        f_data = list(itertools.islice(itertools.cycle(f_data), len_max))

    # Создаем новый список согласно условию:
    new_f = []
    for k in range(len_max):
        a, b = map(float, str(f_data[k])[:-1].split('|'))
        if a > 0 and b > 0:
            new_f.append([f'{str(f_name[k][:-1]).upper():<10}', ':', round(a * b, 1)])
        else:
            new_f.append([f'{str(f_name[k][:-1]).lower():<10}', ':', abs(a * b)])
    return new_f


def write_files(lst: list):
    """Сохраняем данные списка в новый файл."""

    with open(p/'task03'/'third.txt', 'a+', encoding='utf-8') as f:
        for i in range(len(lst)):
            print(*lst[i], end='\n', file=f)


# print(read_name_data('task02', 'name.txt'))
# print(read_name_data('task01', 'data.txt'))
# write_files(lst_new_file(read_name_data('task02', 'name.txt'), read_name_data('task01', 'data.txt')))


        