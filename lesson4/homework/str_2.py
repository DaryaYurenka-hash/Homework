'''
Программа должна запросить несколько цифр через пробел 
    - выдать их общую сумму
    - выдать максимальную цифру
    - выдать среднее арифметическое

'''
count_of_numbers = input("Введите числа через пробел ")
numbers_list = list(map(int, count_of_numbers.split()))
sum_of_numbers = sum(numbers_list)
max_number = max(numbers_list)
arr_numbers = sum(numbers_list) / len(numbers_list)
print(f'Сумма чисел -  {sum_of_numbers}, максимальное число из списка - {max_number}, среднее арифметическое - {arr_numbers}')