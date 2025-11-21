"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""
# Задаем переменные
a1 = 1.3 
a2 = 5
a3 = 3.8
a4 = 9

# Проверка дробных 
if isinstance(a1, float) and isinstance(a2, float) \
    and isinstance(a3, float) and isinstance(a4, float):
    print('True')
else:
    print('False')

#Проверка строковых пар 
if isinstance(a1, str) or isinstance(a2, str) \
    or isinstance(a3, str) or isinstance(a4, str):
    print('True')
else:
    print('False')

# Проверка целочисленных пар
if (isinstance(a1, int) and isinstance(a3, int)) \
    or (isinstance(a2, int) and isinstance(a4, int)) \
    or (isinstance(a3, int) and isinstance(a4, int)):
    print('True')
else: 
    print('False')