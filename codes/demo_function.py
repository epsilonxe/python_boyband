# from demo_input import isMyInputOkay
from math import sqrt, ceil
import sys

def myfactorial(n):
	if isinstance(n, int):
		if n >= 0:
			x = 1
			for i in range(1, n+1):
				x = x * i
		else:
			x = None
	else:
		x = None
	return x


def myfactorialNo2(n):
	if n == 1:
		return 1
	else:
		return n*myfactorialNo2(n-1)


def Fib(a0, a1, n):
	if n <= 0:
		x = []
	elif n == 1:
		x = [a0]
	elif n == 2:
		x = [a0, a1]
	else:
		x = [a0, a1]
		# for i in range(1, n-1):
		# 	y = x[i] + x[i-1]
		# 	x.append(y)
		i = 0
		while i <= n-2:
			i = i + 1
			y = x[i] + x[i-1]
			x.append(y)
	return x


def isprime(n, showprint=False):
	if n <= 1:
		x = False
	else:
		x = True
		max_bound = ceil(sqrt(n))
		if showprint:
			sys.stdout.write(f'[{n}] Complete: ')
			all_round = max_bound - 2
			current_round = 0
		for i in range(2, max_bound):
			if showprint:
				current_round = current_round + 1
				percentage = 100*current_round/all_round
				if current_round == 1 or\
					current_round % 100 == 0 or\
					current_round == all_round:
					if current_round == 1:
						sys.stdout.write(f'{percentage:.2f}%')
						printed_text = f'{percentage:.2f}%'
						sys.stdout.flush()
					elif current_round < all_round:
						deln = len(printed_text)
						sys.stdout.write('\b'*deln)
						sys.stdout.write(f'{percentage:.2f}%')
						printed_text = f'{percentage:.2f}%'
						sys.stdout.flush()
					else:
						deln = len(printed_text)
						sys.stdout.write('\b'*deln)
						sys.stdout.write(f'100% OK\n')
						sys.stdout.flush()
			if n % i == 0:
				x = False
	return x


def find_prime(start, stop):
	x = []
	start = int(start)
	stop = int(stop)
	for i in range(start, stop+1):
		if isprime(i):
			x.append(i)
	return x


def find_factors(n):
	x = []
	for i in range(1, n + 1):
		if n % i == 0:
			x.append(i)
	return x


# Test Functions:

def testPrime():
	print('Test Prime')
	for x in [1233, 99999999999999]:
		print(f"Test {x} is prime? {isprime(x, showprint=False)}")

def testFindPrime():
	print('Test Find Primes')
	print(f"Find primes: {find_prime(1e6,1e6+1000)}")


def testMyFactorial():
	for x in [-3,-2,-1,0,1,2,3,4,5,6,'hello']:
		print(f"Test {x}! = {myfactorial(x)}")
	for x in [1,2,3,4,5,6]:
		print(f"Test {x}! = {myfactorialNo2(x)}")


def testFibonacci():
	print('Test Fibonacci')
	print(Fib(2, 3, 0))
	print(Fib(1, 1, 3))
	print(Fib(2, 3, 3))
	print(Fib(2, 3, 5))
	print(Fib(2, 3, 20))

def testFindFactors():
	for i in [0, 1, 2, 4, 9, 10, 125, 999, 1563]:
		print(f'Factors of {i}: {find_factors(i)}')

# Main program
# testPrime()
testFindFactors()








