"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Декущего ля года
  издания дополнительно проверить на валидность (> 0, <= тгода).

Аксессоры реализоваться через property.
"""

from datetime import datetime

class BookCard():
    
    # С помощью двойного подчеркивания создаем приватные атрибуты
    def __init__(self, author:str, title:str, year:int):
        self.__author = author
        self.__title = title
        self.__year = year
    # Осуществляем контроль доступа с возможностью просмотра
    @property
    def author(self):
      return self.__author
    # Позволяет проверить данные, которые хотим ввести, и позволяет их добавить 
    @author.setter
    def author(self, value):
        if not isinstance(value, str):
          raise ValueError("Автор должен быть строковым значением.")
        self.__author = value
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
      if not isinstance(value, str):
        raise ValueError("Название книги должно быть строковым значением.")
      self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        current_year = datetime.now().year

        if not isinstance(value, int):
          raise ValueError("Год издания должен быть целым числом.")

        if value <= 0 or value > current_year:
          raise ValueError(
                f"Год издания должен быть в диапазоне от 1 до {current_year}."
            )
        self.__year = value

    def __lt__(self, other):
        if not isinstance(other, BookCard):
          return self.year < other.year

    def __le__(self, other):
        if not isinstance(other, BookCard):
          return self.year <= other.year

    def __eq__(self, other):
        if not isinstance(other, BookCard):
          return self.year == other.year
        

books = [
    BookCard("Харуки Мураками", "Норвежский лес", 1987),
    BookCard("Ю Несбё", "Нетопырь", 1997),

    BookCard("Робин Хобб", "Ученик убийцы", 1995),
    BookCard("Робин Хобб", "Королевский убийца", 1996),
    BookCard("Робин Хобб", "Странствия убийцы", 1997),
]
    
books.sort()

for book in books:
    print(f"{book.author} — {book.title} ({book.year})")
