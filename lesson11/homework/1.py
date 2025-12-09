"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: 
        <Бренд-Модель> - Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""

# Создаем класс

class Phone:
    # Определяем атрибуты класса через init, по умолчанию никаких атрибутов не задаем
    def __init__(self, brand: str, model: str, issue_year: int): #специальный метод-конструктор для инициализации объектов
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
# Определяем методы класса
    def receive_call(self, name: str):
        print(f'{self.brand}-{self.model} - Звонит {name}')

    def __str__(self):
        return (
            f"Бренд: {self.brand}\n"
            f"Модель: {self.model}\n"
            f"Год выпуска: {self.issue_year}"
        )

    def get_info(self):
        tupllle = (self.brand, self.model, self.issue_year)
        return tupllle

# Присвоили класс переменной p через __init__
p = Phone("Samsung", "Galaxy S5", 2014)

# Звонит Belhard
p.receive_call("Belhard")

# Получаем инфу о свойствах объекта p класса Phone через tuple
print(p.get_info())

# Выводим полученную с помощью __str__ строку на печать 
print(p) 



