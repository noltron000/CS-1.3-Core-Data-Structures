#!python

def factorial(n):
	'''
	factorial(n) returns the product of the integers 1 through n for n >= 0,
	otherwise raises ValueError for n < 0 or non-integer n
	'''
	# check if n is negative or not an integer (invalid input)
	if not isinstance(n, int) or n < 0:
		raise ValueError(f'factorial is undefined for n = {n}')
	# implement factorial_iterative and factorial_recursive below, then
	# change this to call your implementation to verify it passes all tests
	return factorial_iterative(n)
	# return factorial_recursive(n)

def factorial_iterative(n):
	# initialize total
	total = 1

	while n > 1:
		# loop-multiply total by n
		total *= n
		# subtract multiplier (n) by one before looping again
		n -= 1
	else:
		return total

def factorial_recursive(n):
	# check if n is an integer larger than the base cases
	if n > 1:
		# call function recursively
		return n * factorial_recursive(n - 1)
	else:
		return 1


def main():
	import sys
	args = sys.argv[1:]  # Ignore script file name
	if len(args) == 1:
		num = int(args[0])
		result = factorial(num)
		print(f'factorial({num}) => {result}')
	else:
		print(f'Usage: {sys.argv[0]} number')


if __name__ == '__main__':
	main()
