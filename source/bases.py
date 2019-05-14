#!python
import sys
import math
# math is needed for floor operations.
import string
# string.digits is '0123456789'.
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'.
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
# string.ascii_letters is ascii_lowercase + ascii_uppercase.

LEXICON = string.digits + string.ascii_letters
# LEXICON represents 62 digits in any base numeral systems.


def decode(digits, base):
	'''
	Decode given digits in given base to number in base 10.
	-   base: int → base of given number
	- digits: str → representation of number (in given base)
	- return: int → representation of number (in base 10)
	'''
	# handle up to base 36 [0-9A-Z].
	assert 2 <= base <= 36, f'base is out of range: {base}'
	# numbers read right to left.
	# strings and arrays read left to right.
	# digits need to be reversed to be properly read.
	digits = ''.join(reversed(digits))
	# result stores updated return value.
	result = 0
	# degree is our iterator.
	# it determines the power of our base in the loop.
	degree = len(digits) - 1

	while degree >= 0:
		# mult converts whatever 10...0 is in base-b to base-10.
		# - EX in base-10, 10=10^1, 100=10^2, and 1000=10^3.
		# - EX in base-16, 10=16^1, 100=16^2, and 1000=16^3.
		mult = base**degree
		# place finds the nth-place of the digits string.
		# - EX the 0th-place of 7a059f is 7.
		# - EX the 4th-place of 7a059f is 9.
		place = digits[degree]
		# value is a number < base.
		# it represents a digit's value in base-10.
		# we need to know what a character means numerically.
		# we can do so by finding its index location in LEXICON.
		# list.index(x) finds y where list[y] = x.
		# - EX convert a character to base-10:
		#     hex: | A  | F  | 4  | 9  |
		#     val: | 11 | 15 | 04 | 09 |
		value = LEXICON.index(place)*mult
		# keep track of the current sum.
		# when the loop completes result will be the total sum.
		result += value
		# reduce the degree iterator.
		degree -= 1
	return result


def encode(number, base):
	'''
	Encode given number in base 10 to digits in given base.
	-   base: int → base to convert to
	- number: int → representation of number (in base 10)
	- return: str → representation of number (in given base)
	'''

	# handle up to base 36 [0-9A-Z].
	assert 2 <= base <= 36, f'base is out of range: {base}'
	# handle unsigned numbers only for now.
	assert number >= 0, f'number is negative: {number}'
	# degree represents the number of digits needed in base-n.
	# degree starts at 0.
	# we will find what its max is in the proceeding loop.
	degree = 0

	# this while loop finds the degree stated above.
	# the degree is the first base^power>the number given.
	# it also represents the number of digits for this base.
	while base**degree <= number:
		degree += 1
		# uncomment ↓↓↓ these ↓↓↓ to better understand the loop.
	# 	print(f'@degree {degree-1}:')
	# 	print(f'{base**(degree-1)} is less than {number}.\n')
	# print(f'@degree {degree}:')
	# print(f'{base**degree} is more than {number}.')
	# print('---\n')
	# print(f'The answer has {degree} base-{base} digits.\n')

	# remain stores the remaining amount.
	# remain should always end equal to 0.
	remain = number
	# result stores updated return value.
	result = ''
	# degree is the 1st degree where base^degree is > number.
	# it will transform into the 2nd, 3rd, etc with the loop.
	# degree is also our iterator.
	# it determines the power of our base in the loop.
	# for our loop, we need the last base^degree.
	# it must be greater than our number, so we subtract one.
	degree -= 1

	while degree >= 0 and remain >= 0:
		# value is a number < base.
		# it represents a digit's value in base-10.
		# we need to know what a character means numerically.
		# we can do so by finding its index location in LEXICON.
		# list.index(x) finds y where list[y] = x.
		# - EX convert a character to base-10:
		#     hex: | A  | F  | 4  | 9  |
		#     val: | 11 | 15 | 04 | 09 |
		value = math.floor(remain/base**(degree))
		# here we use value as an index to our LEXICON.
		# this gives us the digit we need.
		result += LEXICON[value]
		# reduce remaining number.
		# it should never go below zero.
		remain -= value*base**degree
		# prepare degree for next iteration.
		degree -= 1

	# make sure function didn't explode before returning.
	not_zero = f'function didn\'t return 0; returned {remain}'
	assert remain == 0, not_zero
	# return resulting string
	return result


def convert(digits, baseX, baseY):
	'''
	Convert given digits in baseX to digits in baseY
	-  baseX: int -- base of given number
	-  baseY: int -- base to convert to
	- digits: str -- representation of number (in baseX)
	- return: str -- representation of number (in baseY)
	'''

	assert 2 <= baseX <= 36, f'baseX is out of range: {baseX}'
	assert 2 <= baseY <= 36, f'baseY is out of range: {baseY}'
	# handle up to base 36 [0-9A-Z].
	value10 = decode(digits, baseX)
	# value10 is the decoded base-10 value of digits.
	return encode(value10, baseY)
	# encode value10 into valueY and return.


def main():
	'''
	Entrypoint when ran from the command-line.
	- reads command-line arguments (expects three)
	- convert given digits between bases
	'''
	# args ignores script file name
	args = sys.argv[1:]
	if len(args) == 3:
		digits = args[0]
		baseX = int(args[1]) # old base
		baseY = int(args[2]) # new base
		# result is the digit converted between bases
		result = convert(digits, baseX, baseY)
		print(f'{digits} in base {baseX}')
		print(f'is {result} in base {baseY}\n')
	else:
		print(f'Usage: \n$ {sys.argv[0]} digits baseX baseY')
		print('Converts digits from baseX to baseY')


if __name__ == '__main__':
	main()
