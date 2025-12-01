"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""
smeshariki_users = [
    {"name": "Крош",      "login": "krosh_",      "password": "123"},     
    {"name": "Ёжик",      "login": "yo zhik",     "password": "111"},     
    {"name": "Бараш",     "login": "barash!",     "password": "baa"},     
    {"name": "Нюша",      "login": "нюша_123",    "password": "love"},   
    {"name": "Копатыч",   "login": "kopatych",    "password": "bee"},    
    {"name": "Лосяш",     "login": "l0syash",     "password": "12345"},  
    {"name": "Пин",       "login": "pin-tech",    "password": "robot"},  
    {"name": "Совунья",   "login": "sovunya",     "password": "owl"},    
    {"name": "Кар-Карыч", "login": "kar karych",  "password": "ret"}
]

def is_valid_login(login: str):
    for ch in login:
        if not (ch.isalnum() or ch == "_"):
            return False
    return True


# Фильтрация слабых паролей (< 5) с помощью lambda и filtred()
weak_passwords = list(filter(lambda user: len(user["password"]) < 5, smeshariki_users))

print("Пользователи со слабыми паролями:")
for user in weak_passwords:
    print(f"- {user['name']}: пароль '{user['password']}' слишком короткий")
print()


# Фильтрация валидных логинов 
valid_logins = list(filter(lambda user: is_valid_login(user["login"]), smeshariki_users))

print("Пользователи с корректными логинами:")

for user in valid_logins:
    print(f"- {user['name']}: логин '{user['login']}' корректный")
print()


# Пользователи с невалидными логинами, используя функцию filter() и lambda
invalid_logins = list(filter(lambda user: not is_valid_login(user["login"]), smeshariki_users))

print("Сообщения пользователям с неправильными логинами:")
for user in invalid_logins:
    print(f"Уважаемый {user['name']}, ваш логин '{user['login']}' не является корректным.")