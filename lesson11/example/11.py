#ООП
    # - свойства (атрибуты, поля ) - характеристики
    # - методы (действия)
    
# class A:
#     pass    

# b = A()
# c = A()
# e = A()

# print(b)


class User:
    password = "1234"
    login = "def_log"
    
    
    @classmethod
    def change_pass(cls, new_pass:str):
        cls.password = new_pass
    
    @staticmethod
    def calc_bd(age):
        return 2005 - age
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.active = True
        self.child = []
        
    
    def __str__(self): # для людей
        return f'{self.name} - {self.age}'
    
    # если нет __str__ принт использует __repr__
    def __repr__(self): # для машин
        return f"User({self.age}, '{self.name}')"
    
    def __len__(self):        
        return len(self.name) + len(self.password)
    
    # obj1 == obj2
    def __eq__(self, other_obj):
        return self.name == other_obj.name
    
    # obj1 < obj2
    def __lt__(self, other_obj):
        return self.age < other_obj.age
    
    # аналогично
    # __ne__(self, other)   obj1 != obj2
    # __le__(self, other)   obj1 <= obj2
    # __gt__(self, other)   obj1 >  obj2
    # __ge__(self, other)   obj1 >= obj2
    
    
    def __call__(self, *args, **kwds):
        print(f"Я {self.name}")
    
    
    def print_info(self):
        print(f"login - {self.login} / pass - {self.password}")



class Users:
    def __init__(self):
        self.users = []
        self.n = 0

    def add(self, user: User):
        self.users.append(user)
        
    def __len__(self):
        return len(self.users)

    def __getitem__(self, val): #obj[0]        
        return self.users[val]
    
    def __setitem__(self, key, value):
        self.users[key] = value
        
    def __iter__(self):        
        return iter(self.users)

    def __next__(self):
        if self.n >= len(self.users):
            raise StopIteration
        res =  self.users[self.n]
        self.n+=1
        return res
        
    
user1 = User('Max', 22)

user1.login = 'user1'
# user1.print_info()

user2 = User('Vasya', 33)
# user2.print_info()

# print(user1.__dict__)
# print(user2.__dict__)

# print(User.__dict__)

User.change_pass('12345')
# user1.__class__.password = '12345'
user3 = User('Vasya', 33) # теперь пароль - 12345 т.к. выше поменяли

print(user1) # __str__
print(len(user1))
print(repr(user1)) # __repr__

print(user2 == user1) # __eq__
print(user2 < user1)  # __lt__


l = [user1, user2]
l.sort(reverse=True) # возможно из-за __lt__
print(l)

user1() # __call__

# ----------------------------
group1 = Users()

group1.add(user1)
group1.add(user2)
group1.add(user3)

print(group1)

print(len(group1)) 

print(group1[2]) # getitem
group1[2] = user2 # setitem
print(group1[2])

for i, user in enumerate(group1, 1):
    print(str(i)*10, user)

print(*group1)
    
# -------------------------------------    
a = 'name123'
setattr(user1, a, 55) # добавить свойство(атрибут) в любой объект
getattr(user1, a) # взять значение свойства(атрибута)
# delattr() # удалить атрибут(свойство)



try:
    print("next", next(group1)) # __next__
    print("next", next(group1)) # __next__
    print("next", next(group1)) # __next__
    print("next", next(group1)) # __next__
except StopIteration:
    print('больше нет')


# ---------------------------


users2 = [
    User('qqq', 22),
    User('ww', 33),
    User('eee', 44),
    User(name='eee', age=44),
]

for user in users2:
    # print(user)
    print(user.name)
    
    


# ---------------------------- Менеджер контекста
# class A:
#     def __init__(self):
#         self.con = 1
    
    
#     def __enter__(self): # срабатывает при создании объекта с помощью with
#         print(1111)
#         return self.con
        
#     def __exit__(self, q, w, e): # срабатывает когда with закончился
#         self.con=0
#         print(2222)


# # a = A()
# # print(333)
# # a.con=0

# with A() as a:
#     print(a)
#     print(333)    