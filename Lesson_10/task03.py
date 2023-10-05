# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.
from datetime import date


class Person:
    __AGE = None
    today = date.today()

    def __init__(self, lastname: str, firstname: str, fathername: str, year, month, day):
        self.lastname = lastname
        self.firstname = firstname
        self.fathername = fathername
        self.year = year
        self.month = month
        self.day = day


    def get_FIO(self):
        return self.lastname, self.firstname, self.fathername

    def birthday(self):
        return self.today.year - self.year - ((self.today.month, self.today.day) < (self.month, self.day))


# a = Person('Иванов', "Семен", "Петрович", 1981, 12, 5)
# a.get_FIO()
# a.birthday()

