# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

# Вернуть список с дублирующимися элементами.
lst_1 = [1, 1,  2, 3, 3, 4, 5, 5, 6, 7, 7, 7]
set_lst_1 = set(lst_1)

for item in set_lst_1:
    lst_1.remove(item)
    while lst_1.count(item) > 1:
        lst_1.remove(item)
print(lst_1)
# В результирующем списке не должно быть дубликатов.
lst = [1, 1,  2, 3, 3, 4, 5, 5, 6, 7, 7]
set_lst = set(lst)
for item in set_lst:
    if lst.count(item) > 1:
        while lst.count(item):
            lst.remove(item)
print(lst)
