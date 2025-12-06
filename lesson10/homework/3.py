"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

"""
a, b, c, d, f = '(()())', '(()()()', '(hello(2)ver()(33)python)', '(hello(2()ver(33)python))', '(hello(2()ver(33)python)'

def open_parentheses(text: str):
    if not isinstance(text, str):
        raise TypeError("Введите строку")
    counter = 0  # Счётчик открытых скобок

    for char in text:
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1

            # Сравнение наличия закрытых и открытых скобок 
            if counter < 0:
                return False

    return counter == 0

