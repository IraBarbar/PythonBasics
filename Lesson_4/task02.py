# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def print_id_char(str_: str):
    ''' Выведет код каждого символа строки по убыванию.'''

    list_ords = []
    for i in str_:
        list_ords.append(ord(i))
    list_unique_ords_str = sorted(set(list_ords), reverse=True)
    for i in list_unique_ords_str:
        print(i)


my_str = '''При передаче аргументов в функцию стоит помнить изменяемого типа объект или
            нет. От этого зависит поменяем мы оригинал или он останется неизменным. Пример
            работы с неизменяемыми переменными'''
print_id_char(my_str)