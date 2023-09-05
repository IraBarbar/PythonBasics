# Задание №7
# Погружение в Python | Коллекции
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.
from pprint import pp
str_user = 'Пользователь вводит строку текста.'
dict_count = {}

for item in set(str_user):
    dict_count.setdefault(item, str_user.count(item))
print(dict_count)

# Вариант 2
dict_count_2 = {}
str_user_2 = list(str_user)
res = 0
for item in str_user:
    while item in str_user_2:
        str_user_2.remove(item)
        res += 1
    dict_count_2.setdefault(item, res)
    res = 0
print(dict_count_2)

# Вариант 3
dict_count_3 = {}
for item in str_user:
    dict_count_3[item] = dict_count_3.get(item, 0) + 1
print(dict_count_3)


