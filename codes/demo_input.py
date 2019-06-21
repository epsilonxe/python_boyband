def printline(symbol = '-', num = 15):
	# c = x
	if isinstance(symbol, str) and isinstance(num, int):
		print(symbol*num)
	else:
		print('')


# def printline():
# 	print('-'*15)

def isMyInputOkay(x):
	if isinstance(x, str):
		text = ''
		if x.isdigit():
			text = 'OK'
		elif '.' in x:
			sx = x.split('.')
			n = len(sx)
			if n > 2:
				text = 'NOT OK'
			elif n == 2:
				frontx = sx[0]
				backx = sx[1]
				if frontx.isdigit() and backx.isdigit():
					text = 'OK'
				elif frontx.isdigit() and backx == '':
					text = 'OK'
				elif backx.isdigit() and frontx == '':
					text = 'OK'
				else:
					text = 'NOT OK'
			elif n == 1:
				text = 'NOT OK'
			elif n == 0:
				pass
		else:
			text = 'NOT OK'
	if text == 'OK':
		return True
	else:
		return False	

def test_input(theinput):
	if isMyInputOkay(theinput):
		print('My input is 100% fine.')
	elif x == 'exit':
		pass
	else:
		print('This is f*cking input.')

def test_printline():
	printline('*', 80)
	printline('+')
	printline(num=2)
	printline(symbol='%')
	printline(symbol='*', num=1)
	printline(num=10, symbol='*')

def areMyInputsOkay(long_string):
	x = long_string.split()
	n = len(x)
	if n > 0:
		all_okay = True
		for i in x:
			if not isMyInputOkay(i):
				all_okay = False
		return all_okay
	elif n == 1:
		return isMyInputOkay(long_string)
	else:
		return False


def test_inputs(x):
	if areMyInputsOkay(x):
		print('Input 100% fine.')
	else:
		print('Bad inputs.')


def find_average(myinput):
	if areMyInputsOkay(myinput):
		x = myinput.split()
		sum = 0
		for i in x:
			sum = sum + float(i)
		n = len(x)
		avg = sum/n
		return avg
	else:
		return None


def test_average(x):
	average = find_average(x)
	print(f"Average of {x} is {average}")



# Main program
# x = ''
# while x != 'exit':
# 	printline()
# 	x = input('Enter your input: ')
# 	# test_input(x)
# 	# test_printline()	
# 	# find_average(x)
# 	# test_inputs(x)
# 	test_average(x)
# print('Exit')




# for i in range(10, 0, -1):
# 	print(f'9 * {i} = {9*i}')
# 	print('-'*9)
# print('STOP')