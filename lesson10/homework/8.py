"""
Написать декоратор который позволит не останавливать программу 
в случае если любая декорируемая функция выбрасывает ошибку, 
а выводить имя функции в которой произошла ошибка и информацию об ошибке в. 
Имя функции можно узнать использовав свойство __name__ ( print(func.__name__))

* сделать настраиваемы параметр который определяет печать в консоль или в файл
и если в файл передать название фала
"""

def decorate_err(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            return print(f'Функция {func.__name__} не выполнена по причине: {err}.')
    return wrapper

@decorate_err
def check(a: int):
    if not isinstance(a, int):
        raise TypeError ('Ошибка ввода данных, введите данные типа int')
    return print(a)

a = 12.5

check(a)






