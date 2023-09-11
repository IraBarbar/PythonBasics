# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def sort_bubble(no_sort_list: list):
    for i in range(1, len(no_sort_list)):
        for j in range(len(no_sort_list)-i):
            if no_sort_list[j] > no_sort_list[j+1]:
                no_sort_list[j+1], no_sort_list[j] = no_sort_list[j], no_sort_list[j+1]


my_list = [10, 3, 4, 5, 20]
print(my_list)
sort_bubble(my_list)
print(my_list)
