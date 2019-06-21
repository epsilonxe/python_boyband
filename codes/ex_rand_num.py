from random import random
from math import ceil

x = ceil(100*random())
y = None
cheat = '^^vv<><>abstart'
print('Try to guess my integer from 0 - 100')
while y != x:
	y = input('Enter your guess: ')
	if y == cheat:
		print(f'Cheat Mode: solution is {x}')
	else:
		y = int(y)
		if y < x:
			print('Your guess is too low.')
		elif y > x:
			print('Your guess is too high.')	
		else:
			print(f'Correct! My number is {x}')
print('Thank you for playing.')

