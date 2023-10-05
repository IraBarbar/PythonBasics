# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.
class Triangle:

    def __init__(self, lenght: float, width=None):
        self.lenght = lenght
        self.width = width if width else lenght

    def perimetr(self):
        return 2 * (self.lenght + self.width)


    def square(self):
        return self.width * self.lenght


a = Triangle(5)
b = Triangle(10, 20)
print(f'Длина {a.lenght} ширина {a.width}\nПлощадь {a.square()}\nПериметр {a.perimetr()}')
print()
print(f'Длина {b.lenght} ширина {b.width}\nПлощадь {b.square()}\nПериметр {b.perimetr()}')


