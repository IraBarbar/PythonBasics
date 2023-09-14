# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def gen_fib(n: int):
    """Генератор чисел Фибоначчи."""

    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(*gen_fib(10))
