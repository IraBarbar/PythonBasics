# Напишите функцию для транспонирования матрицы

def transposition_matrix(lst: list):
    """ Вывод транспонирования матрицы."""

    lst_j = []
    lst_i = []
    for i in range(len(lst[0])):
        for j in range(len(lst)):
            lst_j.append(lst[j][i])
        lst_i.append(lst_j)
        lst_j = []
    for num in lst_i:
        print(num)


lst_matrix = [[1, 2, 3, 4, 5], [11, 21, 31, 41, 51]]
for item in lst_matrix:
    print(item)
print('*' * 10)
transposition_matrix(lst_matrix)
