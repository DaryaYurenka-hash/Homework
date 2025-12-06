"""
Написать генератор последовательности Фибоначчи, 
который принимает максимальное количество чисел в последовательности 
из чисел Фибоначчи и генерирует последовательность. 
Затем  вывести на экран элементы данного генератора. 
Фибоначчи последовательность - первые два числа которой являются 0 и 1, 
а каждое последующее за ними число является суммой двух предыдущих. 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 и так далее.  
"""

def fibonachi(limit: int):
    if not isinstance(limit, int):
        raise TypeError("Введите целое число")
    if limit < 1:
        raise ValueError("Количество чисел должно быть больше нуля")
    a, b = 0, 1 
    count = 0    
    while count < limit: #Если число меньше лимита, то число возвращает , сначала a = 0
        yield a
        a, b = b, a+b    #Затем при следующем next() обращается к этому участку кода, высчитывает новое a и b
        count += 1

gen = fibonachi(12)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))