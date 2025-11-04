'''
Программа должна запросить любую фразу и вывести на экран :
     - количество символов в данной фразе.
     - количество слов  в данной фразе. 
            Словом может считаться любой набор символов разделенный от 
            других пробелом и количеством символов больше или равных 1.
     -* количество гласных в данной фразе. Нельзя использовать if и for.

'''

frase = input('Введите любую фразу: ')
length_of_frase = len(frase)
how_much_words = len(frase.split())
vowel = 'aeuoiy'
how_much_vowel = sum(map(frase.lower().count, vowel))
print(f'In "{frase}" there are {length_of_frase} symbols, {how_much_words} words and {how_much_vowel} vowels')