a = 1
b = 2


def print10():
    for i in range(10):
        print('hello')
   
    
# print('start')

# def print_n(text, n):
def print_n(text: str, n: int = 3, flag: bool = False, 
            param:dict = {'end':'\n',  'sep':' '},
            sep=' '):
    '''
    Выводит на печать text n количество раз
    '''
    
    if flag:
        print(1)
    
    for i in range(n):
        # print(text, sep=param['sep'])
        # print(text, **param)
        print(text, sep=sep)




# print10()
# print_n('hello', 5)

# print(print_n('hello python', flag=True, sep='--'))



# --- проверка и ошибки --------------------------

def s1(a: int, b: int) -> int:
    
    if isinstance(a, int) and isinstance(b, int):
        # ss = a*b
        # return ss
        # или так
        return a*b
    raise TypeError("Неправильный тип")



try:
    s = s1(4, "5")
except Exception as e:
    print(f"---err---\n{e}")
else:
    print(s)

# a = s1("-", 5) # если не проверять тип выполниться неправильно
# print(s1('5', 10))

def s1(a: int, b: int) -> tuple[int, str]:
    err = ''
    s1 = 0
    if isinstance(a, int) and isinstance(b, int):
        s1 = a*b        
    else:
        err = 'err'
    return s1, err
    
res = s1(1, 'ds')
res, err = s1(1, 'ds')
if err:
    print('Ошибка')



# -----------------------------------
print(s1(4, 5))  # позиционные
s = s1(a=4, b=5)  # именованные
print(s)


# -----------------------
def max_n(a, b):
    return a if a > b else b

a1, a2, a3 = 5, 4, 2
print(max_n(max_n(a1, a2), a3))
