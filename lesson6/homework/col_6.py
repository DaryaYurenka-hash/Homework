'''
Запросить 3 раза строку из нескольких чисел через пробел
    - вывести все уникальные числа по возрастанию
    - вывести числа которые есть в каждой строке
    -* вывести числа которые есть только в одной из трех строк
    
    выполнить без циклов и условий
    
    пример:
    >>> 1 2 11 22
    >>> 1 2 22 33
    >>> 1 2 33 44


    1) 1 2 11 22 33 44
    2) 1 2
    3) 11 44
    
'''
# Запрашиваем числа через пробел
counts1 = set(map(int, input('Введите числа через пробел: ').split()))
counts2 = set(map(int, input('Введите числа через пробел: ').split()))
counts3 = set(map(int, input('Введите числа через пробел: ').split()))

# Выводим все уникальные числа по возрастанию
uniq_counts = counts1.union(counts2, counts3)
sorted_uniq_counts = sorted(uniq_counts)

common_counts = counts1.intersection(counts2, counts3)

first_line_uniq = counts1.difference(counts2, counts3)

print(f'Уникальные в трех сетах - {uniq_counts}\nОбщие в трех строках - {common_counts}\n Уникаальные из первой строки - {first_line_uniq}')
