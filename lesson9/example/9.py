
# def f1():
#     # global a
    
#     a = 3
#     a += 1
#     print(222, a)
#     # print(555, locals())
#     def f2():
#         # global a
#         nonlocal a
#         # a = 2
#         a += 1
#         print(666, a)
        
#     f2()
    
# a = 2

# f1()

# # print(444, globals())

# print(3333, a)




# -----------------------------
# рекурсия

# n = 0
# def f1():
#     global n
#     n += 1
#     print(n)
#     f1()
    
# f1()



# def f2(text: str):
#     # if text:
#     #     print(text)
#     #     f2(text[:-1])
#     # return 
#     if not text:
#         return
#     print(text)
#     f2(text[:-1])
    
# f2("Hello PYTHON")


# print(len("asa"))


# ----------------------------------------------
# неограниченное количество параметров/аргументов

# def print_n(*args, sepp ):
#     # print(*args)
#     for a in args:
#         print(a)
    
    
# print_n(1, 2, sepp=" ")


# def f1(*, a, b):
#     pass
# f1(a=1, b=2)
# f1(1, 2) # ошибка - a и b только именованные


# def f2(a1, **kwargs):
#     print(kwargs)
    
# f2(1, a=1, b=2, c="hello")
    
# def f3(a1, *args, **kwargs):
#     print(a1)
#     print(args)
#     print(kwargs)    
    
# f3(9, 1, 2, 3, 4, b=1, c=2)

# def f4(p1,  p2=0, *args, **kwargs):
#     print(p1, p2, args, kwargs)

# f4(123, 111, 1, 5, 10, p2=222, v1=123, v2=1234)
# TypeError: f4() got multiple values for argument 'p2'
# Потому что второй позиционный аргумент "111", он уже назначен p2, 
#   а потом опять p2=111 ещё раз.


# Порядок параметров, который Python ожидает — строго определён для однозначной 
# интерпретации вызова функции:
    # позиционные-only 
    # позиционные или именованные (по умолчанию)
    # *args
    # именованные-only параметры (после *args)
    # **kwargs
    
    # def example(a, b, /, c, d=4, *args, e, f=6, **kwargs):
    #     print(f"a={a}, b={b}, c={c}, d={d}")
    #     print(f"args={args}")
    #     print(f"e={e}, f={f}")
    #     print(f"kwargs={kwargs}")    
    
        # В определении функций символ / используется для обозначения, 
        # что все параметры, объявленные слева от него, являются только 
        # позиционными — их можно передавать в функцию лишь по позиции, а не по имени.




# ----------------------------

# a, b, c = 1, 2, 3, 4
# a, b, *c = [1, 2, 2, 3, 4, 5, 6]
# a, *b, c = [1, 2, 2, 3, 4, 5, 6]
# a, *b, c = 1, 2, 2, 3, 4, 5, 6
# print(a, b, c)

# -----------------------------
# lambda  - анонимная функция

# def f1(x):
#     # s = x+2*2
#     return x+2*2

# print(f1(2))

# a = (lambda x: x+2*2)(2)
# print(a)

# f2 = lambda x: x+2*2

# print(f2(2))

# # a = map(int, ["1", "2", "3"])
# a = map(lambda x: int(x), ["1", "2", "3"])
# a = map(lambda x: int(x)==2, ["1", "2", "3"])
# a = map(lambda x: [i for i in range(int(x))], ["1", "2", "3"])

# print(*a)



# -----------------
# sorted()

# l = ["qwe", 'dsdsda', 'b', 'dsdd']
# l.sort(key=len)
# l.sort(key=lambda x: x[-1])
# sorted(l, key=lambda x: x[-1])
# print(l)


# a = [[11, 2], [2, 4], [1, 5], [8, 3]]
# b = sorted(a, key=lambda x: x[1])

# # сортировка словарей
# d = {1:11, 9:22, 3:33, 4:77, 7:44}
# print(d.items())
# d2 = dict(sorted(d.items(), key=lambda item:item[0])) # сортировка по ключу
# d3 = dict(sorted(d.items(), key=lambda item:item[1])) # сортировка по значению
# print(d2)
# print(d3)



# users = [
#     {'name':'vasia!',
#         'age':25, 
#         'surname':'vasiapupkin!', 
#         'phone':'3752323232'},
#     {'name':'DIma11111111111', 
#         'age':33,
#         'surname':'DimaKr!ivenyz', 
#         'phone':'3752323232'},
#     {'name':'Petia', 
#         'age':21,
#         'surname':'DimaKrivenyz', 
#         'phone':'3752323232'}
# ]

# b = sorted(users, key=lambda user: user['age'], reverse=True)
# b = sorted(users, key=lambda user: len(user['name']), reverse=True)

# print(b)

# # -----------------
# # filter

# def f1(user):
#     return "!" in user['surname']

# users2 = filter(f1, users)

# users2 = filter(lambda user: "!" in user['surname'], users)
# users4 = filter(lambda user: user['age'] > 25, users)

# print(list(users2))





