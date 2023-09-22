# Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).
from lesson_1.HW_5.task07 import gen_simple_nums as gsn
from lesson_1.Lesson_5.task05 import lst_nums as ln
print(*gsn(3))
print(ln())
