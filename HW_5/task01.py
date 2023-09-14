# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


def tuple_path(str_path: str) -> tuple:
    """Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""

    path_ = str_path
    *_, temp = str_path.split('\\')
    name, type_file = temp.split('.')
    return path_, name, type_file


path1 = 'C:\\Users\\Ирина\\IdeaProjects\\D\\exseption\\lesson_1\\HW_5\\task07.py'
print(f' Путь: {tuple_path(path1)[0]}\n Имя файла: {tuple_path(path1)[1]}\n Расширение файла: {tuple_path(path1)[2]}')