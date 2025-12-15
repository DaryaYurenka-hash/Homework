"""
Создать класс Student.


Определить атрибуты:
    - surname - фамилия
    - name - имя
    - group - номер группы
    - grads - список оценок

Определить методы:
    - инициализатор __init__
    - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
    студентов по среднему баллу
    - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
    - метод average_grade -считает и возвращает среднюю оценку ученика

Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 8
"""

# Создаем класс Student
class Student():
    def __init__(self, surname, name, group, grads = []):
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = grads
    
    def add_grade(self, *marks):
        for m in marks:
            if not isinstance(m, int):
                raise TypeError("Введите целое число.")
            if not (1 <= m <= 10):
                raise ValueError("Введите оценку по шкале от 1 до 10.")
            self.grads.append(m)
    
    def average_grade(self):
        if not self.grads:  # если список пустой
            return 0
        total = sum(self.grads)
        count = len(self.grads)
        return total / count
    
    # Делаем красивую строчку вывода данных о студенте со средним баллом, выраженном через float (.2f - точность = сотые)
    def __repr__(self):
        return f"{self.surname} {self.name} (группа - {self.group}) — средний балл: {self.average_grade():.2f}" 
    
    # equal
    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    # not equal
    def __ne__(self, other):
        return self.average_grade() != other.average_grade()
  
    # less than
    def __lt__(self, other):
        return self.average_grade() < other.average_grade()
  
    # greater than
    def __gt__(self, other):
        return self.average_grade() > other.average_grade()
  
    # less than or equal
    def __le__(self, other):
        return self.average_grade() <= other.average_grade()
    
    # greater than or equal
    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()
    
# Присваиваем класс каждому студенту группы
students = [
    Student("Крош",      "Кролик",     101, [8, 9, 10]),
    Student("Ёжик",      "Ежович",     102, [7, 8, 9]),
    Student("Бараш",     "Баран",      101, [6, 7, 8]),
    Student("Нюша",      "Свинка",     103, [10, 9, 10]),
    Student("Копатыч",   "Медведев",   102, [8, 8, 7]),
]

# По возрастанию среднего балла
ascending = sorted(students)         

# По убыванию
descending = sorted(students, reverse=True)  


print("Сортировка по возрастанию:")
for s in ascending:
    print(s)

print("\nСортировка по убыванию:")
for s in descending:
    print(s)

# Студенты со средним баллом > 8 
print("\nСтуденты со средним баллом больше 8:")
for s in students:
    if s.average_grade() > 8:
        print(s)