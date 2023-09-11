# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.
from pprint import pp

def dict_sum_bonus(list1: list[str], list2: list[int], list3: list[str]) -> dict:
    """ Возвращает словарь ключ - имя: значение - премия."""

    def replace_percent(str1):
        return int(str1.replace("%", ""))

    list3 = list(map(replace_percent, list3))
    return dict(zip(list1, list(num2 * num1 // 100 for num1, num2 in zip(list2, list3))))


list_name = ['Ваня', 'Петя', 'Катя']
list_bid = [200, 250, 150]
list_bonus = ['10%', '10%', '10%']
pp(dict_sum_bonus(list_name, list_bid, list_bonus))

