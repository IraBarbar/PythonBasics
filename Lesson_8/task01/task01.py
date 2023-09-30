# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
from lesson_1.Lesson_7.task03.task03 import read_name_data
import json
from pathlib import Path
import os
os.chdir('..')
p = Path(Path().cwd())


def made_js_file(old_lst: list) -> dict:
    """Преобразует список списков в словарь,."""

    new_dict = {}
    for i in old_lst:
        x, y = str(i)[:-1].strip().split(':')
        x, y = str(x).strip(), str(y).strip()
        a = str(i)[0].upper()
        new_dict[a + x[1:]] = y
    return new_dict


def write_json_file(old_lst: list, path_: str):
    """Преодразует список в словарь и записывает в файл по строчно."""

    res = json.dumps(made_js_file(old_lst), indent=2, sort_keys=True, ensure_ascii=False)
    with open(path_, 'a+', encoding='utf-8') as f:
        print(res, end='\n', file=f)


print(old_file := read_name_data(p / "Lesson_7" / "task03", 'third.txt'))
write_json_file(old_file, 'Lesson_8\\task01\\new_file.json')




