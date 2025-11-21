'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''

# Запрашиваем три числа, присваивая их в переменные a, b, c

a = int(input('Введите число'))
b = int(input('Введите число'))
c = int(input('Введите число'))

# Вводим ветвление c if

if a > b:
    if a > c:
        print(a)
    else: 
        print(c)
else: 
    if b > c:
        print(b)
    else:
        print(c)

# Используя elif 

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)