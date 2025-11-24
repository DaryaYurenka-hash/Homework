
# while (пока)- когда не знаем сколько повторов
# for - когда знаем сколько раз повторить, или что то перебрать



# --- WHILE -----------------------------------

# while 1: #  бесконечно. Остановить - ctrl+С
# # while True    
#     print(1)
#     print(222)
#     print(333333)
    
# print('ok')

# a = 1
# b = 2
# while a < 10 and b == 2:
#     # if a == 5:
#     #     a += 1
#     #     continue # пропускает итерацию
    
#     if a == 5:
#         break # останавливает цикл
            
#     print(a)    
#     a += 1

# print('ok')    # выполниться когда  закончиться цикл 

# -----------------------------

# pas = input("pas: ")

# while pas != '1234':
#     print('err')
#     pas = input("pas: ")
#     if pas == 'stop':
#         break
# else:
#     print('else')

# print('ok')

# -----------------------


# menu = '''
# 1 - ПОГОДА
# 2 - АНЕКДОТ
# 3 - КУРСЫ ВАЛЮТ
# 0 - ВЫХОД
# '''

# res = input(menu)

# while res != '0':
#     if res == '1':
#         print(1)
#     elif res == '2':
#         print(2)
#     elif res == '3':
#         print(3)
#     else:
#         print('err')
#     res = input(menu)
#     # break
    
# -------------------------

# a = 0 
# a = 1 
# b = "Hello"
# # while 1:
# # while a:
# while b:
#     print(b)
#     b = b[:-1]
    
# ------------------------------------------

          #[0, 1, 2, 3, 4]
# for i in range(5):
#     print(i)

# for i in range(1, 50, 5):
#     # i = 4
#     # print(i)
#     print(i+1, "номер - " + str(i))
    

# a = range(10) # от 0 по 9
# a = range(10, 50)
# a = range(10, 50, 5)
# print(list(a))

# for i in range(3):
#     pass

# for i in range(3):
#      print(i)
# else:
#     print('ok')

# for i in "12345":
#     print(i)
    
# for _ in "12345":
#     print('Hello')    


# for i in "___":
#     print(i*50)

# bad_symbol = "!@#$%^&*()"
# login = 'Vasya123@!'
# for s in login:
#     if s in bad_symbol:
#         print("errr", s)
#     # print(s)

# ----------------------------------
    
# users = ["user1", "user2", "user3", "user4"]

# for user in users:
#     print(user)

# i = 1
# for user in users:
#     print(i, user)    
#     i += 1

    
# for i in range(len(users)):
#     print(i+1, users[i])    

# print(list(enumerate(users)))


# for i, user in enumerate(users):
#     print(i, user)

# --------------------------------------


# a = [
#   [1, 2, 3],
#   [3, 4, 5],
#   [7, 8, 8],
# ]

# for i in a:
#     for j in i:
#         print(i, j)

# -----------------------------------

# users = [
#     {"name":"Vasya1", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya2", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya3", "login":"vva@siiiia!",  "age":23},    
#     {"name":"Vasya4", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya5", "login":"vvasiiiia!",  "age":23},    
#     {"name":"Vasya6", "login":"vv#asiiiia",  "age":23},    
#     {"name":"Vasya7", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya8", "login":"vvasiiiia!",  "age":23}
# ]

# for user in users:
#     print(user)


# for user in users:
#     print(user['name'], user['age'])



# for user in users:
#     for key in user:
#         print(key, user[key], user['age'])
#         # print(user[key], end=' ')
        
        

# user = {"name":"Vasya", "login":"vasya123",  "age":23}

# for i in user:
#     print(i, user[i])        
        
# for v in user.values():
#     print(v)        
    
# for user in user.items():
#     print(user, user[0], user[1])    
    
# for key, val in user.items():
#     print(key, val)        
    
# -------------------------------

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [8, 9, 0]

# for i1, i2, i3 in zip(a, b, c): # перебор двух или более списков
#     print(i1, i2, i3)    