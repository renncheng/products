# python test product

import os #operating system

#load file
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品' in line:
				continue # jump to the next loop
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
	return products

#user input
def user_input(products):
	while True:
		name = input('Please key in produce name, press "q" to quit. ')
		if name == 'q':
			break
		price = input('Please key in price. ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

#print record
def print_record(products):
	for p in products:
		print('The price of ', p[0], 'is ', p[1])

#write file
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品Product,價格Price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # check file exist or not
		print('yeah! the file exists!')
		products = read_file(filename)
	else:
		print('There is no this file!')
	products = user_input(products)
	print_record(products)
	write_file('products.csv', products)
	
main()