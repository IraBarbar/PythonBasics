# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
import os
from pathlib import Path
import json
import csv
import pickle


def wolk_dir(path: str):
    dirs_path = []
    dir_names = []
    file_name = []
    for dir_path, dir_name, file_name in path:
        # print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
        dirs_path.append(dir_path)

    """Собираем все именя в один лист:"""
    dir_list = []
    for i in dir_names+dirs_path+file_name:
        if len(i) != 0:
            dir_list.append(i)
    print(dir_list)

    """Создаем json файл"""
    dict_dir = {}
    pp = Path(Path().cwd())
    for obj in dir_list:
        if os.path.isdir(obj):
            dict_dir['директории'] = dict_dir.get('директории', []) + [obj]
            print(f'{obj = }', "- это директория")
        if os.path.isfile(obj):
            dict_dir['файлы'] = dict_dir.get('файлы', []) + [obj]
            print(f'{obj = }', "- это файл")
    res = json.dumps(dict_dir, indent=2, sort_keys=True, ensure_ascii=False)
    with open(pp/'info_dirs.json', 'w', encoding='utf-8') as f:
        print(res, end='\n', file=f)

    """Создаем csv файл"""
    with open('quest.csv', 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=['директории', 'файлы'],
                                   dialect='excel', delimiter='#', quotechar='=', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerow(dict_dir)

    """Создаем пикле"""
    with open(pp/'my_dict.pickle', 'wb') as f:
        pickle.dump(dict_dir, f)

                                       
# os.chdir('..')
p = os.walk(os.getcwd())
wolk_dir(p)