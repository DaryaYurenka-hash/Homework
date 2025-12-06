
"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial(a: int):
    # Проверка введенного числа
    if not isinstance(a, int):
        raise TypeError("Введите целое число")
    if a < 0:
        raise ValueError('Введите положительное число')
    # Задаем базовое значение факториала
    n = 1
    fact = 1
    # Пока n ≤ a, генерируем следующий факториал"
    while n <= a:
        fact *= n
        # yield возвращает текущий факториал наружу, если в последствии мы пишем next при вызове функции 
        yield fact
        n += 1

gen_f = factorial(7)

print(next(gen_f))
print(next(gen_f))
print(next(gen_f))
print(next(gen_f))
print(next(gen_f))
print(next(gen_f))
print(next(gen_f))