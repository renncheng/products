# python test product
products = []

while True:
	name = input('Please key in produce name, press "q" to quit. ')
	if name == 'q':
		break
	price = input('Please key in price. ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)
