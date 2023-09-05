# Задание №6
# Погружение в Python | Коллекции
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

str_user = 'Пользователь вводит строку текста. Вывести каждое слово с новой строки.'

str_user = sorted(str_user.split())

# for item in str_user:
#     if len(item) > max_:
#         max_ = len(item)

max_ = len(max(str_user, key=len))

for i in range(len(str_user)):
    print(f'{(i+1):>3}. {str_user[i]:>{max_ }}')

for i in range(len(usr := sorted(input("Введите строку: ").split()))):
    print(f'{str(i + 1) + ".":>{len(str(len(usr))) + 1}} {usr[i]:>{max([len(usr[i]) for i in range(len(usr))])}}')
