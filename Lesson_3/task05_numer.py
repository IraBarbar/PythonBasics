# Задание №5
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.
import random
lst = [-1, 4, 6, -8, 2, 2, -10, 11]
negotive_index_lst = []
for i in range( len(lst)):
    if lst[i] % 2:
        negotive_index_lst.append(i+1)
print(negotive_index_lst)

print(lst_2 := sorted([random.randint(0, 10) for _ in range(20)]))

new_lst = [i + 1 for i in range(len(lst_2)) if lst_2[i] % 2]
print(new_lst)
