# Fibonacci: 1, 1, 2, 3, 5, 8, 13, ...
def fib(m):
	x = 1
	y = 1
	while x < m:
		print(x)
		x, y = y, x+y
fib(100)			

		

