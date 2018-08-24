# python test product
products = []

while True:
	name = input('Please key in produce name, press "q" to quit. ')
	if name == 'q':
		break
	price = input('Please key in price. ')
	products.append([name, price])
print(products)
