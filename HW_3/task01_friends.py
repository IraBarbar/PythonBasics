# Задание №8
# Погружение в Python | Коллекции
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

dict_friends_things = {
    'Nike': ('tent', 'matches', 'flashlight', 'blanket', 'pillow',),
    'Igor': ('pillow', 'boiler', 'spray', 'soap',),
    'Vlad': ('soap', 'water', 'food', 'battery',),
}
dict_friends_things['Masha'] = ('battery', 'spray', 'radio', 'pillow',)
print('Какие вещи взяли все три друга:')
for key, val in dict_friends_things.items():
    print(f'\t{key:<7}: {sorted(val)}')
print()

print('Какие вещи уникальны, есть только у одного друга:')
set_things = ()
for val in dict_friends_things.values():
    set_things += val
print(f'\t{set(set_things)}')
print()

print('Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует:')
set_unic_things = set()
for i in set_things:
    if set_things.count(i) == len(dict_friends_things) - 1:
        set_unic_things.add(i)
for key, val in dict_friends_things.items():
    for i in set_unic_things:
        if i not in val:
            print(f'\t{key} dis not  {i}')







