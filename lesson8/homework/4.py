'''

Написать функцию, которая возвращает любое число в виде денежной величины 
с разделителями групп разрядов в качестве пробела и валютой в конце. 
Денежная величина всегда должна содержать количество копеек в виде двух 
знаков после точки, даже если исходное число целое. 
*Нельзя использовать форматную строку.
Например: 1234567 -> "1 234 567.00 руб."

с помощью try перехватить возможные ошибки.
'''

def money_eqv(number, currency='BYN'):
    try:
        # пробуем преобразовать ввод в число
        number = float(number)
    except ValueError:
        print("Ошибка: введите число")
        return
    
    # округляем до 2 знаков после запятой
    number = round(number, 2)
    number_str = str(number)

    # разделяем целую и дробную часть
    if '.' in number_str:
        int_part, dec_part = number_str.split('.')
    else:
        int_part = number_str
        dec_part = '00'

    # гарантируем 2 знака после точки
    if len(dec_part) == 1:
        dec_part += '0'
    elif len(dec_part) > 2:
        dec_part = dec_part[:2]

    # формируем группы по 3 цифры с конца
    money_parts = []
    part = ''
    for digit in int_part[::-1]:  # идём с конца
        part = digit + part
        if len(part) == 3:
            money_parts.append(part)
            part = ''

    if part:  # если остались 1–2 цифры
        money_parts.append(part)

    # склеиваем группы через пробел
    int_part_with_spaces = ''
    for i, grp in enumerate(money_parts[::-1]):
        if i == 0:
            int_part_with_spaces = grp
        else:
            int_part_with_spaces = int_part_with_spaces + ' ' + grp

    # формируем финальную строку
    money_string = int_part_with_spaces + '.' + dec_part + ' ' + currency
    return money_string




b = input('Введите число')
money_eqv(b)