'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''
def factorial(a:int):
    # Проверка типа данных
    if not isinstance(a, int):
        raise TypeError("Аргумент должен быть целым числом")
    # Проверка на неотрицательность
    if a < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    # Базовый случай
    if a == 0:
        return 1  
    elif a > 0:
        return a * factorial(a-1)  
    
a = int(input('Введи число:'))    
    
print(factorial(a))