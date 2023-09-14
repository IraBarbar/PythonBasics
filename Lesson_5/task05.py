# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.
from typing import Any, Generator


def lst_nums():
    new_lst = []
    for n in range(1, 101):
        if n % 15 == 0:
            new_lst.append('FizzBuzz')
        elif n % 3 == 0:
            new_lst.append('Fizz')
        elif n % 5 == 0:
            new_lst.append('Buzz')
        else:
            new_lst.append(n)
    return new_lst


gen_nums = ('FizzBuzz' if num % 15 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num
            for num in range(1, 101))


for i in gen_nums:
    print(i)

# for j in lst_nums():
#     print(j)
