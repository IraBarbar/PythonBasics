# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
from sys import argv

def test_year(year: int):
    if year > 1582:
        if year % 4 == 0 and year % 100 != 0:
            return True
        elif year % 100 == 0:
            if year % 400 == 0:
                return True
    else:
        return False


def test_date(str_DD_MM_YYYY: str) -> bool:
    """Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна"""

    if all(str(x).isdigit() for x in str_DD_MM_YYYY.split('.')):
        day, month, year = map(int, str_DD_MM_YYYY.split('.'))
        if day not in range(1, 32) or month not in range(1, 13) or year not in range(1, 10000):
            return False
        if day > 30 and month in [4, 6, 9, 11]:
            return False
        if month == 2 and day > 28 and test_year(year) != True:
            return False
        if month == 2 and day > 29 and test_year(year) == True:
            return False
        else:
            return True
    else:
        return False

