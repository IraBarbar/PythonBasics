# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного числа используйте код:
#
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1_000
MORE = 'больше'
LESS = 'меньше'
GOOT = 'Верно!'
COUNT = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)


while COUNT > 0:
    num_from_user = int(input(f'Компьютер загадал число *** от {LOWER_LIMIT} до {UPPER_LIMIT} ***. Угадай ! : '))

    if num_from_user == num:
        print(GOOT)
        break
    elif num_from_user > num:
        print(LESS)
        UPPER_LIMIT = num_from_user
    elif num_from_user < num:
        print(MORE)
        LOWER_LIMIT = num_from_user
    COUNT -= 1
    print(f'Осталось попыток: {COUNT} ')
    print()
else:
    print(f'Закончились попытки. Компьютер загадал {num}')


