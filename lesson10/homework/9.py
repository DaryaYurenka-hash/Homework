"""
Написать функцию hello, которая принимает 2 аргумента name и surname и
выводит принтом "Привет, {name} {surname}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
Выполняеся функция <имя> с аргусентами <аргументы> 
После выполнения функции напечатать строку "<имя функции> - завершена"
"""

def log_decorator(func): #
    def wrapper(*args): #предположим, что мы не знаем, какие аргументы будут представлены в func, тогда *args, **kwargs
        # Указываем строки принта в будущем порядке вывода
        print(f'Выполняеся функция {func.__name__} с аргументами {args}') #
        result = func(*args) 
        print(f"{func.__name__} - завершена")
        return result # wrapper возвращает result
    return wrapper # а декоратор возвращает wrapper

# Оборачиваем в декоратор рандомную функцию
@log_decorator
def invitation(name, surname):
    print(f'{name} {surname} you are a magician.')

# Вызываем аргументы через строку ввода
name = input('Name: ')
surname = input('Surname: ')

# Применяем функцию приветствия
invitation(name, surname)