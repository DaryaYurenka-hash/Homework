"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""
def yes_or_no(collection):
   if not all(isinstance(digit, int) for digit in collection):
            raise TypeError ("Введите числв в список")
   
   else:
        digit_collection = set() # Задаем множество(в нем нет повторов) digit_collection и список result, чтобы наполнять множество уникальными значениями из collection,
        result = []              # а result значениями yes или no

        for digit in collection:

            if digit in digit_collection: # если digit есть во множестве, то добавляем в список "да"
                 result.append('yes')

            if digit not in digit_collection: # если digit нет во множестве, то добавляем в список "нет" и добавляем digit во множество
                 result.append('no')
                 digit_collection.add(digit)     

        return result
           
