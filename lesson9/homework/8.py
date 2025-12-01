'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''
smeshariki_users = [
    {"name": "Крош",      "login": "krosh_",      "password": "123",      "active": True},
    {"name": "Ёжик",      "login": "yo_zhik",     "password": "111",      "active": False},
    {"name": "Бараш",     "login": "barash!",     "password": "baa",      "active": True},
    {"name": "Нюша",      "login": "nyusha_123",  "password": "love",     "active": False},
    {"name": "Копатыч",   "login": "kopatych",    "password": "bee",      "active": True},
    {"name": "Лосяш",     "login": "l0syash",     "password": "12345",    "active": True},
    {"name": "Пин",       "login": "pin_tech",    "password": "robot",    "active": False},
    {"name": "Совунья",   "login": "sovunya",     "password": "owl",      "active": True},
    {"name": "Кар-Карыч", "login": "kar_karych",  "password": "ret",      "active": False},
]

# Ищем строковые значения в словаре по ключу field_name, проверяя value с помощью isinstance()

only_strings = [
    {field_name: value for field_name, value in user.items() if isinstance(value, str)}
    for user in smeshariki_users
]

print(only_strings)


# Ищем булевые значения в словаре по ключу field_name, проверяя value с помощью isinstance()

only_bools = [
    {field_name: value for field_name, value in user.items() if isinstance(value, bool)}
    for user in smeshariki_users
]

print(only_bools)
