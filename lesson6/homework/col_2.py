"""
2. Создать структуру данных сотрудников фирмы с 
    тремя сотрудниками. каждый сотрудник должен иметь:
        ФИО, 
        должность, 
        год рождения, 
        список навыков, 
        список детей с их именем и годом рождения. 
    
    Запросить ФИО сотрудника и вывести по нему информацию.
    
    ** задать вопрос о желании добавить сотрудника,
        если ответ да - добавить сотрудника через несколько input
        (после добавления сотрудника вывести всю структуру консоль)

"""
employees = [
    {
        "Name": "James Smith",
        "Position": "Manager",
        "Year of birth": 1978,
        "Skills": ["Sales", "Management"],
        "Children": ["Clara, 2003", "Charles, 1998"]
    },
    {
        "Name": "Helen Rodriges",
        "Position": "Software Engineer",
        "Year of birth": 1995,
        "Skills": ["Python", "Git"],
        "Children": ["Elizabeth, 2015", "George, 2020"]
    },
    {
        "Name": "Rose Miller",
        "Position": "Graphic Designer",
        "Year of birth": 2002,
        "Skills": ["Photoshop", "Figma"],
        "Children": ["Veronika, 2024", "Michael, 2021"]
    }
]

# Создаем список имен сотрудников emp_list из списка employees, чтобы сверить name_of_employee
emp_list = [employees[0]["Name"], employees[1]["Name"], employees[2]["Name"]]

# Вводим с консоли ФИО сотрудника
name_of_employee = input('Введите ФИО для поиска: ')

# Проверяем наличие названного сотрудника в списке emp_list
check_of_search =  emp_list.index(name_of_employee)

# Выводим данные по найденному сотруднику name_of_employee
result_of_search = employees[check_of_search]
print(result_of_search)

#  ** задать вопрос о желании добавить сотрудника
question = str(input('Введите "Да", если хотите добавить сотрудника: ')).lower()

if question == "да":
    name = input('Enter the name of an employee: ')
    position = input('Enter the position of an employee: ')
    year_of_birth = input('Enter Year of birth: ')
    skills = input('Enter the Skills (через запятую): ').split(", ")
    children = input('Enter the Children info (через запятую): ').split(", ")

    dict4 = {
        "Name": name,
        "Position": position,
        "Year of birth": year_of_birth,
        "Skills": skills,
        "Children": children
    }

employees.append(dict4)

# Пример данных для проверочки:)

#"Name": "Hose Ferras",
#"Position": "Graphic Designer",
#"Year of birth": 1990,
#"Skills": ["Photoshop", "Figma"],
#"Children": ["Leonidas, 2011", "Diego, 2012"]

# Выводим всю структуру в консоль
print(employees)