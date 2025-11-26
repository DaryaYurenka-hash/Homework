'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''
def count_char(string: str):
    try:
        string = str(string)
    except:
        raise TypeError('Введите строковое значение')
    
    string_dict = {}
    for char in string:
        if char == ' ':          # пропускаем пробел
            continue
        if char in string_dict:
            string_dict[char] += 1 #увеличиваем на 1 значение соответсвующей буквы, если вхождений несколько
        else:
            string_dict[char] = 1 #если вхождение 1, то 1
    
    return string_dict #возвращаем словарик






