# python test product

import os #operating system

#load file
products = []
if os.path.isfile('products.csv'): # check file exist or not
	print('yeah! the file exists!')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品' in line:
				continue # jump to the next loop
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('There is no this file!')

#user input
while True:
	name = input('Please key in produce name, press "q" to quit. ')
	if name == 'q':
		break
	price = input('Please key in price. ')
	price = int(price)
	products.append([name, price])
print(products)

#print record
for p in products:
	print('The price of ', p[0], 'is ', p[1])

#write file
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品Product,價格Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
