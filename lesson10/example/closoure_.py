# def f2():
#     print(123)

# a = f2
# a()

# def f1(y):
#     x = 11
#     def wrapper(b):
#         print(1, x, y, b*y)
#     return wrapper

# a1 = f1(1)
# a2 = f1(2)

# a1(2)
# a2(2)

# print(a1.__closure__[0].cell_contents)
# print(a1.__closure__[1].cell_contents)

# ----------------------



def print1(a):
    def wrapper(b):
        print(f"{a}{' - ' if a else ''}{b}")
    return wrapper

pr_err = print1("Error")
pr_info = print1("Внимание")
pr = print1("")

pr_err("Пароль неверный") # перед сообщением будет слово Error
pr_info("В пароле должно быть более 7 символов")
pr("Ok")

# map(print1("Error"), [1, 2])

    
        