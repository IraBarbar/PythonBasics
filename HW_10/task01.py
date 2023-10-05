# Задание
# 📌 Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.
from lesson_1.Lesson_10.task05 import *


class Dog(Animals):

    def __init__(self, name: str, age: int, color):
        super().__init__(name, age)
        self.color = color

    def show_color(self):
        print('Цвет:', self.color)

    def show_kind(self):
        print('Вид:', 'собака')

    def show_all_info(self):
        self.show_name()
        self.show_age()
        self.show_color()
        self.skills()
        self.show_kind()
        print()


class Bob(Dog):

    def __init__(self, name='Боб', age=2, color='серый'):
        super().__init__(name, age, color)


Bob().show_all_info()   