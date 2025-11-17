'''
Дан список
['samsung', 'lg', 'xerox', 'bosch']
Удалить элемент с именем 'xerox'
Добавить элемент на 2 место 'indesit'

'''

# Создаем список
l = ['samsung', 'lg', 'xerox', 'bosch']

# Удаляем элемент по индексу
l.pop(2)

# Вставляем элемент 'indesit' на индекс 2
l.insert(2, 'indesit')

# Выводим новый список
print(l)
