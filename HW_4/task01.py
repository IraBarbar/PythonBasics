# Напишите функцию для транспонирования матрицы

def transposition_matrix(lst: list):
    """ Вывод транспонирования матрицы."""

    lst_temp = []
    lst_position = []
    for i in range(len(lst[0])):
        for j in range(len(lst)):
            lst_temp.append(lst[j][i])
        lst_position.append(lst_temp)
        lst_temp = []
    return lst_position


lst_matrix = [[1, 2, 3, 4, 5], [11, 21, 31, 41, 51]]
for item in lst_matrix:
    print(item)
print('*' * 10)
for num in transposition_matrix(lst_matrix):
    print(num)
