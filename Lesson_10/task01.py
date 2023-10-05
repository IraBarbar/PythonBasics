# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
import math


class Circle:

    def __init__(self, radius: float):
        self.radius = radius

    def circumference(self):
        """Метод возвращает длину окружности."""

        return round(2 * math.pi * self.radius, 2)

    def square_circle(self):
        """Метод возвращает площадь круга"""

        return round(math.pi * (self.radius ** 2), 2)


c1 = Circle(5)
print(f'Радиус = {c1.radius}:\n'
      f'Длинна окружности = {c1.circumference()}\n'
      f'Площадь = {c1.square_circle()}')
