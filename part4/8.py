def simple(y):

	if y <= 1: print(y, 'not prime')

	x = y // 2

	for i in range(y, 1, -1):
		if x <= 1:
			print(y, 'is prime')
			break
		elif (y % x == 0):
			print(y, 'has factor', x)
			break
		x -= 1


simple(3)
simple(4)
simple(5)
simple(6)
