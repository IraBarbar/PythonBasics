# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь
from lesson_1.Lesson_10.task03 import Person
import random


class Work(Person):
    def __init__(self, lastname: str, firstname: str, fathername: str, year, month, day):
        super().__init__(lastname, firstname, fathername, year, month, day)
        self.ID = random.randint(100_000, 1_000_000)
        self.level = sum(list(map(int, str(self.ID)))) % 7

    def get_id(self):
        return self.ID

    def get_level(self):
        return self.level


work1 = Work('Иванов', "Сергей", "Петрович", 1930, 8, 5)
work2 = Work()
print(*work1.get_FIO(), work1.birthday(),  work1.get_id(), work1.get_level())
