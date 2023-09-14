# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def gen_simple_nums(count_simple_nums: int) -> list:
    """Функция генерирует N простых чисел, начиная с числа 2."""

    lst_nums = set()
    if count_simple_nums > 0:
        lst_nums.add(2)
    num = 3
    while len(lst_nums) < count_simple_nums:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            lst_nums.add(num)
        num += 1
    yield sorted(lst_nums)


for k in gen_simple_nums(200):
    print(k)

