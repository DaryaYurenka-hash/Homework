"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""
temp_day = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}

result = dict(sorted(temp_day.items(), key=lambda item: item[1]))
result_reversed = dict(sorted(temp_day.items(), key=lambda item: item[1], reversed = True))

# temperature.items() создает пары день, температура, затем с помощью key указываем индекс элемента с температурой [1]
# Аргумент key — говорит sorted, по чему сортировать
# Аргумент reverse=True — сортировка в обратном порядке