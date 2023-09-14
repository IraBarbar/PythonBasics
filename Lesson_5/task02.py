# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

def dict_word_chr(str_: str) -> dict:
    """ Cловарь, где ключ — буква, а значение — код буквы."""

    return {item: ord(item) for item in [i for i in str_ if i.isalpha()]}


str1 = 'Итератор — это объект, представляющий поток данных; объект возвращает \
        данные по одному элементу за раз. Итератор Python должен поддерживать \
        метод с именем __next__ (), который не принимает аргументов и всегда  \
        возвращает следующий элемент потока.'

# for key, val in dict_word_chr(str1).items():
#     print(f'{key}: {val}')

iter_dict_word_chr = iter(dict_word_chr(str1).items())
print(next(iter_dict_word_chr))
print(next(iter_dict_word_chr))
print(next(iter_dict_word_chr))
print(next(iter_dict_word_chr))
print(next(iter_dict_word_chr))
print(next(iter_dict_word_chr))
print(next(iter_dict_word_chr))


