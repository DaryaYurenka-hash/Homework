# list() - списки
# tuple() - кортежи - защищенный список
# dict() - словари
# set() - множества
# frozenset()

# # ------------------------ tuple
# cor = (12, 24)
# green = (0, 255, 0)
# # rgb = [100, 200, 55]
# rgb = 100, 200, 55
# print(rgb, type(rgb))

# a = (1) # int
# a = (1,) # tuple
# print(a, type(a))

# a = [1, 2, 3]
# b = tuple(a)
# print(b)


# -------------------------------- dict

# {ключ:значение, ключ2:значение2}

# d = {}
# d = dict()
# print(d)

# d = {1:"111", 2:"222", 3:333}

# ---- создаем словари

# key (ключи) - только неизменяемые типы данных
# value (значения) - любые типы данных

# a = {"a":11, "b":22, "c":"Hello"}
# b = dict(a=11, b=22, c='Hello')
# print(a, b)

# sp = [("key1", "value1"), ("key2", "value2")]
# c = dict(sp)
# print(c)

# d1 = dict.fromkeys(["key1", "key2"], "value")
# d2 = dict.fromkeys(["key1", "key2"])
# print(d1, d2)



# user = ["Вася", 33, True]
# user = {"name":"Вася", "age":33, "active":True, 
#             "phones":["11111", "22222"], 
#             "phones2":{
#                 "mts":"111111", 
#                 "vel":"222222"
#             }
# }
# print(user["name"])
# print(user["phones"][0])
# print(user["phones2"]["mts"])


# user['name'] = "Петя" # меняет
# user['name1'] = "Петя" # создает новый ключ

# users = [
#     {"name":"Vasya1", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya2", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya3", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya4", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya5", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya6", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya7", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya8", "login":"vvasiiiia",  "age":23}
# ]

# print(users[3]['login'])


# users1 = {
#     1:{"name":"Vasya1", "login":"vvasiiiia",  "age":23},    
#     2:{"name":"Vasya2", "login":"vvasiiiia",  "age":23},        
#     99:{"name":"Vasya2", "login":"vvasiiiia",  "age":23},        
#     # 88:{"name":"Vasya2", "login":"vvasiiiia",  "age":23},        
#     "ivanov":{"name":"Vasya2", "login":"vvasiiiia",  "age":23},        
    
# }

# users1[1]
# users1['ivanov']
# users1['ivanov']['age']

# # --------------------------------
# a = {"a":11, "b":22, "c":"Hello"}
# print(list(a.values())) # значения
# print(*a.values(), sep="\n")

# print(list(a.keys())) # ключи

# print(list(a.items())) # элементы
# print(list(a.items())[2][1])

# из элементов повторно можно создать словарь
# b = list(a.items())
# print(b)
# c = dict(b)
# print(c)

# взять элемент
# print(a['b']) # если нет ключа выдаст ошибку
# print(a.get('bb')) # если нет ключа выдаст None
# print(a.get('bb', "нет")) # если нет ключа выдаст "нет"

# # объединить словари
# d1 = {"key1":"value1"}
# d2 = {"key2":"value2"}
# d3 = {"key3":"value3"}
# d1.update(d2) # добавить к словарю второй словарь, меняет словарь d1
# d5 = d2 | d3 # сложить два словаря - не меняет d1 d2 - возвращает объединенный
# print(d1)
# print(d5)

# удаление элементов
# del a["b"]
# b = a.pop('c')
# c = a.popitem()
# print(a, b, c)

# setdefault(key[, default]): Возвращает значение по ключу, если ключ существует, иначе добавляет ключ со значением



# ---------------------------------------------- SET
# коллекция из уникальных значений

# a = [1, 2, 3, 1, 2, 5]

# b = set(a)
# print(b)

# a = {1, 1, 2, 3, 3, 4}
# print(a, type(a))

# a = set("Hello Pythonnnn")
# print(a)

# b = frozenset(a)
# print(b, type(b))

# ---------------------------------------


# a = {8, 3, 1, 5 }
# # b = {6, 7, 8, 3}
# b = {8, 1, 3}


# print("-"*30)
# # Включает ли set другой set
# print(a.issubset(b)) # все элементы a принадлежат b.
# print( a <= b )

# print(a.issuperset(b)) # все элементы b принадлежат a.
# print( a >= b )


# #объединение и пересечение

# print(a | b) # об] объединить
# print(a.union(b)) # объединить

# print(a.intersection(b)) # пересечение - только общие
# print(a & b)

# print(a.difference(b)) # разность - есть только в первом
# print(a - b)

# print(a.symmetric_difference(b)) # есть в обоих но не общие
# print(a ^ b)




