# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.
import decimal
import math
from decimal import Decimal
d = 30
decimal.getcontext().prec = 42
sqw_round = Decimal((d ** 2 / 4 * math.pi))

print(sqw_round)