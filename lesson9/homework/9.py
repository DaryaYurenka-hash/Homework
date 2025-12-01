"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").

Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def dict_from_args(*args, **kwargs):
    # --- Проверка и сумма позиционных аргументов ---
    if not all(isinstance(x, int) for x in args):
        raise TypeError("Все позиционные аргументы должны быть целыми")
    args_sum = sum(args)
    
    # --- Проверка и максимальная длина значений именованных аргументов ---
    if not all(isinstance(v, str) for v in kwargs.values()):
        raise TypeError("Все аргументы - ключевые слова должны быть строками")
    
    if kwargs:
        kwargs_max_len = max(len(v) for v in kwargs.values())
    else:
        kwargs_max_len = 0  # если kwargs пустой, длина 0
    
    # --- Возврат словаря ---
    return {
        "args_sum": args_sum,
        "kwargs_max_len": kwargs_max_len
    }

result = dict_from_args(1, 2, 3, 5, 7, name="Krosh", login="kroshik")
print(result)