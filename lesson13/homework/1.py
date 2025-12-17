"""
Создать класс User с атрибутами:

Свойства:
	- name - имя - содержит только буквы русского алфавита 
	- login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия: 
                содержит менее шести символов
                содержит строчную букву
                содержит заглавную букву
                содержит число
	- is_blocked - заблокирован
	- subscription_date - дата до какой действует подписка
	- subscription_mode - вид подписки (free, paid)


Методы:
	- bloc - принимает логическое значение и помечает пользователя заблокированным 
	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату. 
						Если дата не передана значит на дату проверки. 
						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
	- change_pass - смена пароля и присваивание его в качестве действующего. 
						Пароль должен пройти валидацию. 
						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.



Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. 
Логин и пароль должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
Валидацию данных сделать через регулярные выражения
"""
# Помогает работать с проверкой символов по системе ascii
import string
import random
from datetime import datetime, timedelta

class User:
	def __init__(self, name: str, login, password:str = None):
		self.name = name
		self.login = login 
		if password is not None:
			self.password = password
		else:
			self.password = self.generate_password()
			print(f"Сгенерированный пароль: {self.password}")
	
		self.is_blocked = False
		self.subscription_date = datetime.now() + timedelta(days=30)
		self.subscription_mode = 'free'
    
	@staticmethod
	def generate_password():
		while True:
			length = random.randint(4, 5)  # меньше 6 символов
			chars = string.ascii_letters + string.digits
			pwd = ''.join(random.choices(chars, k=length))
			if (any(ch.islower() for ch in pwd) and any(ch.isupper() for ch in pwd) and any(ch.isdigit() for ch in pwd)):
				return pwd
			
	# Параметр имени
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, value):
		if not isinstance(value, str):
			raise TypeError('Введите имя типа string.')
        
		if not value.isalpha():
			raise ValueError('Введите имя, состоящее только из букв.')
        
		russian_letters = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        
		if not all(ch in russian_letters for ch in value.lower()):
			raise ValueError('Имя должно состоять из символов кириллицы')
		
		self._name = value

	# Параметр логина
	@property
	def login(self):
		return self._login

	@login.setter
	def login(self, value):
		if not isinstance(value, str):
			raise TypeError('Введите имя типа string.')

		if len(value) < 6:
			raise ValueError('Длина логина должна быть не менее 6 символов.')

		allowed_chars = set(string.ascii_letters + '_' + string.digits)

		if not all(ch in allowed_chars for ch in value):
			raise ValueError('Логин должен состоять из латинских букв, допускается нижнее подчеркивание "_".')
		
		self._login = value

	# Параметр пароля
	@property
	def password(self):
		return self._password
	
	@password.setter
	def password(self, value):
		if not isinstance(value, str):
			raise TypeError('Введите пароль типа string.')
        
		if not value.isalnum():
			raise ValueError('Введите пароль, состоящий только из букв и цифр.')
		
		allowed = (string.ascii_letters + string.digits)

		if not all(ch in allowed for ch in value):
			raise ValueError('Пароль должен состоять только из латинских букв и цифр.')
		
		if not any(ch.isupper() for ch in value):
			raise ValueError('Введите хотя бы 1 заглавную букву.')
		
		if not any(ch.islower() for ch in value):
			raise ValueError('Введите хотя бы 1 строчную букву.')
		
		if not any(ch.isdigit() for ch in value):
			raise ValueError('Введите хотя бы 1 число.')
		
		if len(value) >= 6:
			raise ValueError('Длина должна быть менее 6 символов.')
		
		self._password = value

	def bloc(self, flag: bool):
		"""Блокирует или разблокирует пользователя"""
		self.is_blocked = flag

	def check_subscr(self, check_date: datetime = None):
		"""Проверка подписки"""
		if check_date is None:
			check_date = datetime.now()
		active = check_date <= self.subscription_date
		days_left = max((self.subscription_date - check_date).days, 0)
		return {
			'active': active,
			'mode': self.subscription_mode,
			'days_left': days_left
		}

	def change_pass(self, new_password: str = None):
		"""Смена пароля"""
		if new_password:
			self.password = new_password
		else:
			self.password = self.generate_password()
			print(f"Сгенерированный пароль: {self.password}")

	def get_info(self):
		"""Вывод информации о пользователе"""
		if self.is_blocked:
			return f"Пользователь {self.name} заблокирован"
		return (
			f"Имя: {self.name}\n"
			f"Логин: {self.login}\n"
			f"Пароль: {self.password}\n"
			f"Подписка: {self.subscription_mode} до {self.subscription_date.date()}\n"
			f"Заблокирован: {self.is_blocked}"
		)


    
           
# Создаем пользователей
# harry = User('Гарри', 'HarryP1', 'Hp1A')
hermione = User('Гермиона', 'HermioneW', 'Hw1B')
# ron = User('Рон', 'RonWeas', None)
# dumbledore = User('Альбус', 'Dumbledore', 'Ad1C')

# # Вывод информации
# print(harry.get_info())
# print(hermione.get_info())
# print(ron.get_info())  
# print(dumbledore.get_info())


# # Проверка подписки на сегодня
# print('Проверка подписки Гарри:', harry.check_subscr())


# # Блокируем Рона
# ron.bloc(True)
# print(ron.get_info())

# Смена пароля Гермионы
print(hermione.get_info())
hermione.change_pass('NewH1')
print(hermione.get_info())

# # Генерация нового пароля для Гарри
# print(harry.get_info())
# harry.change_pass()
# print(harry.get_info())		


