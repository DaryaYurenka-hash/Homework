"""
Запросить у пользователя год рождения и в соответствии с его возрастом 
охарактеризовать пользователя - 
ребенок, подросток, юноша, в расцвете сил, пожилой, старик.
"""
# Запрашиваем год рождения, считаем простым выражением примерный возраст пользователя
age = 2025 - int(input('Enter your birth year: '))

# Включаем оператор ветвления
if age < 0 or age > 130:
    print('not born or already dead')
elif age < 12:
    print("kid")
elif age < 18:
    print("teenager")
elif age < 25:
    print("youth")
elif age < 56:
    print("mature adult")
elif age < 75:
    print("Elderly person")
else:
    print("old person")
