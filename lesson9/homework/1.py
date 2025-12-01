"""
Написать функцию print_n() которая будет печатать переданный текст, 
но при этом перед этим текстом выводить строку с номером отражающим 
какой раз по счету выполняется эта функция. 

"""

counter = 0

def print_n(text: str):
    global counter
    try:
        text = str(text)
        counter += 1
        print(f"{counter}: {text}")
    except Exception:
        raise TypeError("Введите строковое значение")
    

print_n('Вот ОН, а дальше уже Ариана Гранде,')
print_n("Леди Гага")
print_n('и все остальные')


