# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.


gen_num = (num for num in range(101) if num % 2 == 0 and (num % 10 + num // 10 != 8))
for i in gen_num:
    print(i)

