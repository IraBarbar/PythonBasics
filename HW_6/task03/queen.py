# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
import random
COUNT_QUEENS = 8   # количество ферзей на доске


def lst_queens():
    lst1 = []
    i = random.randint(1, 8)
    j = random.randint(1, 8)
    lst1.append([i, j])

    while len(lst1) < COUNT_QUEENS:
        i = random.randint(1, 8)
        j = random.randint(1, 8)
        if [i, j] not in lst1:
            k = 0
            while k < len(lst1):
                if lst1[k][0] == i:
                    break
                if lst1[k][1] == j:
                    break
                k += 1
            else:
                lst1.append([i, j])
    return lst1


def test_queen(lst_1: list) -> bool:
    """Если ферзи не бьют друг друга верните истину, а если бьют - ложь."""

    lst_1 = sorted(lst_1)
    for k1 in range(COUNT_QUEENS - 1):
        for m2 in range(k1+1, COUNT_QUEENS):
            if lst_1[k1][1] == lst_1[m2][1] or lst_1[k1][0] == lst_1[m2][0]:
                return False
    for kd in range(COUNT_QUEENS - 1):
        for md in range(1, 9):
            if [lst_1[kd][0] + md, lst_1[kd][1] - md] in lst_1:
                # print(f'{[lst_1[kd][0] , lst_1[kd][1]]} бъет {[lst_1[kd][0]+md, lst_1[kd][1]-md]}')
                return False
            if [lst_1[kd][0] + md, lst_1[kd][1] + md] in lst_1:
                # print(f'{[lst_1[kd][0] , lst_1[kd][1]]} бъет {[lst_1[kd][0] +md , lst_1[kd][1] + md]}')
                return False
    return True


def lst_queens_is_true():
    lst = []
    while len(lst) < 4:
        temp = lst_queens()
        if test_queen(temp) == True:
            lst.append(sorted(temp))
        temp = []
    return lst


def show_queens():

    lsts = lst_queens_is_true()
    for lst in lsts:
        print(lst)
        for i in range(1, 9):
            l1 = []
            for j in range(1, 9):
                if [i, j] in lst:
                    l1.append('Q')
                else:
                    l1.append('*')
            print(*l1)
        print()





