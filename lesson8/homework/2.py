'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''

def rectangle(length: float, width: float, param: str = 'per'):
    """
    Возвращает площадь или периметр прямоугольника.
    Параметры:
        length (float): длина
        width (float): ширина
        param (str): 'per' — периметр, 'sq' — площадь
    """
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        raise TypeError("Неправильный тип данных. Длина и ширина должны быть числами.")
    param = param.lower()
    if param == 'per':
        return 2 * (length + width)
    elif param == 'sq':
        return length * width
    raise ValueError("Неизвестный параметр param. Используйте 'per' или 'sq'.")

print(rectangle(3, 4, 'sq'))
    