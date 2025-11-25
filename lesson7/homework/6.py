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
    name = input('Введите имя (или "stop" для выхода): ').strip()
    if name.lower() == 'stop':
        break

    recommendations = input('Оставьте свой отзыв (или "stop" для выхода): ').strip()
    if recommendations.lower() == 'stop':
        break

    review.append({'name': name, 'recommendations': recommendations})

print(review)

# Количество отзывов
print(f"Количество отзывов: {len(review)}")

# Имена пользователей
names = []
for r in review:
    names.append(r['name'])
print("Имена пользователей:", names)

# Отзывы
recommendations_list = []
for r in review:
    recommendations_list.append(r['recommendations'])
print("Отзывы пользователей:", recommendations_list)