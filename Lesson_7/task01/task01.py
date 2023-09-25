# Задание №1
# # ✔ Напишите функцию, которая заполняет файл
# # (добавляет в конец) случайными парами чисел.
# # ✔ Первое число int, второе - float разделены вертикальной чертой.
# # ✔ Минимальное число - -1000, максимальное - +1000.
# # ✔ Количество строк и имя файла передаются как аргументы функции.
import random
MIN_NUM = -1000
MAX_NUM = 1000

def write_file(text_data: str, cnt_line: int):
    """Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел"""

    lst = []
    while len(lst) < cnt_line:
        text = str(random.randint(MIN_NUM, MAX_NUM)) + '|' + str(random.uniform(MIN_NUM, MAX_NUM))
        lst.append(text)
    with open(f'{text_data}.txt', 'a+', encoding='utf-8') as f:
        if f.tell() != 0:
            f.writelines('\n')
        f.writelines('\n'.join(lst))
    print('Успешно!')


# write_file('data', 2)