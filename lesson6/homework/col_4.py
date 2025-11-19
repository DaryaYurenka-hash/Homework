'''
Буква "a" стоит 10 очков, "b" - 20, "c" - 30, "d" - 40
Запросить кодовою фразу из пяти символов используя только a, b, c, d.
Вывести на экран общее количество очков введенной фразы.

'''
# Создаем словарь
score_rate_values = {'a': 10, 'b' : 20, 'c': 30, 'd': 40}

# Вводим кодовое слово
code = list(str(input('Введите кодовое слово: ')).lower())

# Считаем количество букв
sc_count_a = code.count('a')
sc_count_b = code.count('b')
sc_count_c = code.count('c')
sc_count_d = code.count('d')

# Считаем общий рейтинг введенного слова
common_cs = sc_count_a * score_rate_values['a'] + sc_count_b * score_rate_values['b'] + sc_count_c * score_rate_values['c'] + sc_count_d * score_rate_values['d']

# Выводим на экран результат
print(f'Общее количество баллов = {common_cs}')




