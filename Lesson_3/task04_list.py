# Задание №4
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

my_list = [11, 11, 1, 2, 3, 1, 2, 3, 3, 5, 5, 7, 6, 7, 6, 4, 9, 8, 9, 9, 10, 10]

i = len(my_list) - 1
FLAG = True
while FLAG:
    if my_list.count(my_list[i]) == 2 :
        temp = i
        i -= 1
        my_list.remove(my_list.pop(temp))
    i -= 1
    if i < 0:
        FLAG = False
print(my_list)



