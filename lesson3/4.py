'''
запросить число и вывести на экран сколько номиналов в этом числе:
	 - тысячи
	 - сотни
	 - десятки
	 - единицы

пример: # знак >>> значит что ввели что-то через input
    >>> 21234 
    тысяч - 21
    сотни - 2
    десятки - 3
    единицы - 4
'''


number = int(input('Enter a number = '))
thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10
print(f'Thousands - {thousands}, Hundreds - {hundreds}, Tens - {tens}, Ones - {ones}', sep='\n')
