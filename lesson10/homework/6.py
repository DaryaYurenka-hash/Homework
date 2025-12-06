"""
Написать генератор triangular_numbers, который возвращает подряд 
треугольные числа

Формула:
Tn = 1 / 2 * n * (n + 1)

Например:
tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""

def triangular_numbers(n: int):
    if not isinstance(n, int):
        raise TypeError("Введите целое число.")
    if n < 1:
        raise ValueError("n должно быть больше или равно 1.")

    for k in range(1, n + 1):
        tr = k * (k + 1) // 2
        yield tr
# Генератор считает треугольное число для каждого n от 1 до заданного значения. 
# При применении next мы получаем каждое значение до указанного нами n


gen = triangular_numbers(7)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))