# Задание №6
# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку

# Как смогла  😮‍💨 

gen_multiplication_table_1 = ([(str(i) + ' * ' + str(j) + ' = ' + str(i*j) + '   \t')
                              for i in range(2, 6)] for j in range(2, 10))

gen_multiplication_table_2 = ([str(i) + ' * ' + str(j) + ' = ' + str(i*j) + '    \t'
                              for i in range(6, 10)] for j in range(2, 10))

for k in gen_multiplication_table_1:
    print(*k)

print()

for k in gen_multiplication_table_2:
    print(*k)

