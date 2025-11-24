# List comprehension - условно "генераторы списков"
from pprint import pprint

# a = []
# n = 9
# for i in range(1, n+1):
#     sq = i**2
#     if i<5:
#         a.append(sq)
    
# print(a)    

# b = [i**2 for i in range(1, n+1)]
# # b1 = [str(i) for i in range(1, n+1)]


# b = [i**2 for i in range(1, n+1) if i < 5]
# b = [i**(2 if i%2==0 else 3) for i in range(1, n+1) if i < 5]

# print(b)

# -----------------------------------------

users = [
    {"name": "Vasya1", "login": "vvasiiiia",  "age": 23},
    {"name": "Vasya2", "login": "vvasiiiia",  "age": 23},
    {"name": "Vasya3", "login": "vva@siiiia!",  "age": 23},
    {"name": "Vasya4asas", "login": "vvasiiiia",  "age": 12},
    {"name": "Vasya5", "login": "vvasiiiia!",  "age": 23},
    {"name": "Vasya6", "login": "vv#asiiiia",  "age": 12},
    {"name": "Vasya7", "login": "vvasiiiia",  "age": 23},
    {"name": "Vasya8", "login": "vvasiiiia!",  "age": 23}
]

users1 = [user['name'] for user in users]
users1 = [[user['name'], user['age']] for user in users]
users1 = [user for user in users if user['age']<18]

user1 = [name.lower() for name in [user['name']
                      for user in users if user['age'] == 12]]

pprint(users1)


users2 = {f"key{i+1}":user['name'] for i, user in enumerate(users)}
users2 = {user['name']:user['login'] for user in users}

print(users2)