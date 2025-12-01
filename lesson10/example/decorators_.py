# def f1(f, a=1):
#     def wrapper(*args, **kwargs):
#         print(111)
#         res = f(*args, **kwargs)
#         print(222, f.__name__)
#         return res
#     return wrapper
    
# def f11(f, a=1):
#     def wrapper(*args, **kwargs):
#         print(11111)
#         res = f(*args, **kwargs)
#         print(22222, f.__name__)
#         return res
#     return wrapper    


# @f1
# @f11
# def f2(t):
#     print(f'Hello1 {t}' )

# f2_nc = f2.__closure__[0].cell_contents
    
# @f1
# def f3():
#     print('Hello2')
#     return 123456789
    
# def f4():
#     print('Hello3')        
    
# # f1(f2)


# f2('python')
# print(f3())


# map(f2, [1, 2, 3])



# ---------------------------------



# ------------------------------
# декораторы с настройкой параметров
    
def loging(filename='3.txt'):
    # print(filename)
    def _loging(func):
        def wrapper(*args, **kwargs):
            with open (filename, "a", encoding='utf8') as f:
                from time import time, ctime, strftime
                # f.write(f"{ctime()} - запущена {func.__name__}\n")
                f.write(f"{strftime('%M:%S')} - запущена {func.__name__}\n")                
            func(*args, **kwargs)
                                        
        return wrapper
    return _loging


@loging(filename="lesson10\\example\\log1.txt")
def f1():
    a = 1+1
    
@loging(filename="log2.txt")
def f2():
    a = 1+1
    
@loging()
def f3():
    a = 1+1
    
f1()
         