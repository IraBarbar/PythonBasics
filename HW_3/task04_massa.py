# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
from random import sample
import math
# максимальный вес:
WEIGHT = 15

dict_things = {
    'чайник': 2,
    'плед': 7,
    "вода": 5,
    "полатка": 11,
    "консерва": 2,
    'розжиг': 4,
    'фонарик': 3,
}
# возможное количество сочетаний:
COUNT_ = math.factorial(len(dict_things))

dict_option = {}
set_ = set()
res = 0
i = 1
data = list(dict_things.items())

while COUNT_:
    r = sample(data, len(dict_things))
    dict_option.setdefault(i, set_)
    for item in r:
        if res + int(item[1]) <= WEIGHT:
            res += item[1]
            set_.add(item)
        
    if i > 1:
        for j in range(1, i):
            if dict_option.get(i) == dict_option.get(j):
                dict_option.pop(i)
                i -= 1
                break
    i += 1
    set_ = set()
    res = 0
    COUNT_ -= 1


for key, val in dict_option.items():
    print(f'{key:<3}: {str(sorted(val)):<70} = {sum([sorted(val)[i][1] for i in range(len(sorted(val)))])} ')

