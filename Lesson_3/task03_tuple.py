# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.
from pprint import pp

tuple_types= (5, 'Plat', 5.20, 'Ola', -2, 3.1415)
dict_types = {'int': [], 'float': [], 'str': []}
dict_types_2 = {}
dict_types_3 = {}
for item in tuple_types:
    if isinstance(item, int):
        dict_types['int'].append(item)
    elif isinstance(item, float):
        dict_types['float'].append(item)
    else:
        dict_types['str'].append(item)
for key, values in dict_types.items():
    print(f'{key}: {values}')

print('*' * 20)
for item in tuple_types:
    if type(item) not in dict_types_2:
        dict_types_2[type(item)] = []
    dict_types_2[type(item)].append(item)

for key, values in dict_types_2.items():
    print(f'{key}: {values}')

print('*' * 20)
for item in tuple_types:
    dict_types_3.setdefault(type(item), [])
    dict_types_3[type(item)].append(item)
pp(dict_types_3)
