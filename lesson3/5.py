'''
Запросить количество секунд. 
Вывести на экран время в формате ЧЧ:ММ:СС равное эти секундам.
Пример: 35457 -> 09:50:57
Сделать 2 варианта с форматной строкой и без.
'''

seconds = int(input('Seconds = '))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')
print(hours, minutes, seconds, sep=':')