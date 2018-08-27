# python test product
products = []

while True:
	name = input('Please key in produce name, press "q" to quit. ')
	if name == 'q':
		break
	price = input('Please key in price. ')
	price = int(price)
	products.append([name, price])
print(products)

for p in products:
	print('The price of ', p[0], 'is ', p[1])

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
