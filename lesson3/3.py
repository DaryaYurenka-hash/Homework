'''
запросить цену закупки телефона и выдать следующую информацию.
	- цена продажи (+30% к цене закупке)
	- цена продажи со скидкой 5%
	- цена продажи со скидкой 10%
	- цена продажи со скидкой 15%
'''
smartphone_price = int(input('smartphone price = '))

print(smartphone_price + smartphone_price * 0.3)
print(smartphone_price - smartphone_price * 0.05)
print(smartphone_price - smartphone_price * 0.1)
print(smartphone_price - smartphone_price * 0.15)
