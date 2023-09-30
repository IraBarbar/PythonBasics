# Напишите функцию группового переименования файлов. Она должна:
# 1. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# 2. принимать параметр количество цифр в порядковом номере.
# 3. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# 4. принимать параметр расширение конечного файла.
# 5. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.
# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

import os
from pathlib import Path


def rename_files(new_file_: str,  py_new, cnt: int, count_int: int, new_element='_'):
    file_name = []
    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')

    """нашли и присвоили значения старого названия из каталога"""
    old_nums = []
    pys_old = []
    old_element = '_'
    old_names = []
    for file_ in file_name[:-1]:
        temp, py_old = file_.split('.')
        pys_old.append(py_old)
        old_name, old_num = str(temp).split(old_element)
        old_names.append(old_name)
        old_nums.append(old_num)

    """Цикл переименования"""
    for i in range(cnt):
        j = str(i).zfill(count_int)
        p = Path(f'{old_names[i]}{old_element}{old_nums[i]}.{pys_old[i]}')
        print(p.rename(f'{new_file_}{new_element}{j}.{py_new}'))


rename_files('old', 'txt', 20, 15)