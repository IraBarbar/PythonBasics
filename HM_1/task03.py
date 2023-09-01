# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

LOWER_LIMIT = 1
UPPER_LIMIT = 100_000
NUM_SIMPLE = 'Число  является простым.'
NUM_COMPOSITE = 'Число  является составным.'
NUM_ERROR = 'Неверный диапозон чисел.'
num = int(input(f'Введите целое число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
i = 1
if LOWER_LIMIT <= num <= UPPER_LIMIT:
    while i < num:
        if num % i == 0 and i != 1:
            print(NUM_COMPOSITE)
            break
        i += 1
    else:
        print(NUM_SIMPLE)
else:
    print(NUM_ERROR)