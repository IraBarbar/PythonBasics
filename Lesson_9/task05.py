# Задание №5
# 📌 Объедините функции из прошлых задач.
# 📌 Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# 📌 Выберите верный порядок декораторов.

from lesson_1.Lesson_9.task02 import decor as dc2
from lesson_1.Lesson_9.task03 import decor as dc3
from lesson_1.Lesson_9.task04 import count as cn


@cn(2)
@dc3
@dc2
def func_cnt(num: int, cnt: int):
    cnt_user = 0
    print(f'У вас {cnt} попыток')
    while cnt:
        cnt_user += 1
        num_user = int(input('Введите число:'))
        if num == num_user:
            print(s := f"Вы угодали число {num} за {cnt_user} попыток.")
            return s

        if num_user > num:
            print('Меньше')
        if num_user < num:
            print('Больше')
        cnt -= 1
    else:
        print(s := f'Вы не отгадали число {num} за {cnt_user} попыток.')
        return s


func_cnt(12, 1)