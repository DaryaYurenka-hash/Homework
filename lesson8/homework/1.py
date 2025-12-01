"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев


"""
 
def namesurname(fio: str, param: str = 'iof'):
    if not isinstance(fio, str):
        raise TypeError("Неправильный тип данных. Введите текст.")
    parts = fio.split()
    surname, name, patronymic = parts
    io = name[0] + '.' + patronymic[0] + '.'
    if len(parts) != 3:
        raise ValueError("ФИО должно содержать три слова: Фамилия Имя Отчество.")
    if param == 'iof':
        print(io + surname)
    elif param == 'fio':
        print(surname + ' ' + io)


namesurname('Юренко Дарья Игоревна', 'fio')
    

        
    

