'''
Написать функцию, которая вычисляет факториал переданного в нее числа без рекурсии.

'''
def factorial(a: int) -> int:
    if not isinstance(a, int) or a < 0: #проверяем тип введенных данных
        raise TypeError("Введите положительное целое число")
    
    result = 1
    for i in range(1, a + 1): 
        result *= i
    return result

print(factorial(5))
print(1*2*3*4*5)