"""
1. Запросить у пользователей имя и отзыв о магазине. 
Программа должна запрашивать данные пока не введено слово "stop". 
Все данные сложить в словарь.
    -распечатать количество отзывов
    -распечатать отдельно имена пользователей
    -распечатать отдельно отзывы

"""

# Почему цикл while выполняет только строку name = input... , а далее не запрашивает recommendations = input... ? 
review = []

while True:
    name = input('Введите имя (или "stop" для выхода): ')
    if name.lower() == 'stop':
        break

    recommendations = input('Оставьте свой отзыв (или "stop" для выхода): ')
    if recommendations.lower() == 'stop':
        break

    review.append({'name': name, 'recommendations': recommendations}) #Заполняем спимсок словариком

# Количество отзывов
print(f"Количество отзывов: {len(review)}")

# Имена пользователей
names = []
for r in review:
    names.append(r['name']) #достаем нужную инфу из словарика по ключу и вставляем в список
print("Имена пользователей:", names)

# Отзывы
recommendations_list = []
for r in review:
    recommendations_list.append(r['recommendations']) #достаем нужную инфу из словарика по ключу и вставляем в список
print("Отзывы пользователей:", recommendations_list)