# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
import random


def gen_name():
    min_len = 4
    max_len = 7
    vowels = 'аеёиоуыэюя'
    first_letters = 'аеёиоуэюябвгджзклмнпрстфхчш'
    letters = 'аеёиоуыэюябвгджзйклмнпрстфхцчшщ'
    name = str(random.choice(first_letters)).upper() + \
        (random.choice(vowels)) + \
        ''.join(random.sample(letters, random.randint(2, 5)))
    return name


# with open(f'name.txt', 'a+', encoding='utf-8') as f:
#     if f.tell() == 0:
#         print(gen_name(),  file=f)
#     for i in range(8):
#         print(gen_name(), end='\n', file=f)
