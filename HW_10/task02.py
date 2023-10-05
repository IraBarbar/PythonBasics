# 📌 Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.
class MultiplicationTable:

    def __init__(self):

        gen_multiplication_table_1 = ([(str(i) + ' * ' + str(j) + ' = ' + str(i * j) + '   \t')
                                       for i in range(2, 6)] for j in range(2, 10))

        gen_multiplication_table_2 = ([str(i) + ' * ' + str(j) + ' = ' + str(i * j) + '    \t'
                                       for i in range(6, 10)] for j in range(2, 10))

        for k in gen_multiplication_table_1:
            print(*k)

        print()

        for k in gen_multiplication_table_2:
            print(*k)


a = MultiplicationTable()


class Fib:

    def gen_fib(num: int):
        """Генератор чисел Фибоначчи."""

        a, b = 0, 1
        for _ in range(num):
            yield a
            a, b = b, a + b


print()
print(*Fib.gen_fib(11))
