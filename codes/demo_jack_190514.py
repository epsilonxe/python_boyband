x = input("Enter names and surnames: ")
# print(x)
y = x.split()
# print(y)
n = len(y)
if n % 2 == 0:
	i = 0
	numman = 0
	while i <= n - 1:
		name = y[i]
		surname = y[i+1]
		# numman = numman + 1
		# print(f"Person {numman}: {name} {surname}")
		print(f"Person {(i/2)+1:.0f}: {name} {surname}")
		i = i + 2
else:
	print('Input not complete.')
