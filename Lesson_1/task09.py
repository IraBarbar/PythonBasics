# Задание №9
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

i = 2

while i < 10:
    for j in range(2, 11):
        print(f' {i} * {j} = {i * j:<3}\t'
              f' {i + 1} * {j} = {(i + 1) *j:<3}\t'
              f' {i + 2} * {j} = {(i + 2) *j:<3}\t'
              f' {i + 3} * {j} = {(i + 3) *j:<3}\t')
    i += 4
    print()
