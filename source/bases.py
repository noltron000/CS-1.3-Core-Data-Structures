#!python

import math
import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

# a GRAPHEME is the smallest meaningful contrastive unit in a writing system
# it represents a number whose maximum is determined by whatever base system being used - 1
GRAPHEMES = string.digits + string.ascii_lowercase + string.ascii_uppercase

def decode(digits, base):
	"""Decode given digits in given base to number in base 10.
	digits: str -- string representation of number (in given base)
	base: int -- base of given number
	return: int -- integer representation of number (in base 10)"""

	# we have to reverse digits to iterate correctly!
	digits = "".join(reversed(digits))

	print(f'---DECODE--- digs: {digits} base: {base}')
	# Handle up to base 36 [0-9A-Z]
	assert 2 <= base <= 36, f'base is out of range: {base}'
	# Handle unsigned numbers only for now
	# assert number >= 0, f'number is negative: {number}'
	# Iterate through digits string
	# i: degree iterator
	i = len(digits) - 1
	print(f'digits {i + 1}')
	# result: return keeper
	result = 0

	while i >= 0 :
		# value is a number < base, representing a digit's value in base-10
		# it is found by looking up its index in the graphemes string
		# hex: | A  | F  | 4  | 9  |
		# val: | 11 | 15 | 04 | 09 |
		value = GRAPHEMES.index(digits[i])*base**i
		print(f'i: {i} -- digits[i]: {digits[i]} -- value: {value}')
		result += value
		i -= 1

	return result

def encode(number, base):
	"""Encode given number in base 10 to digits in given base.
	number: int -- integer representation of number (in base 10)
	base: int -- base to convert to
	return: str -- string representation of number (in given base)"""
	### print(f'\n---encode function--- num:{number} base:{base}')
	# Handle up to base 36 [0-9A-Z]
	assert 2 <= base <= 36, f'base is out of range: {base}'
	# Handle unsigned numbers only for now
	assert number >= 0, f'number is negative: {number}'
	# Find out first n where (base**degree > number)
	# n+1 turns out to be number of digits needed
	degree = 0
	while base**degree <= number:
		### print(f'@degree {degree}: {base**degree} is less than or equal to {number}')
		degree += 1
	### print(f'@degree {degree}: {base**degree} is more than {number}')
	### print(f'There are {degree} base-{base} digits the answer\n')

	# i: degree iterator
	i = degree - 1
	# remain: number iterator
	remain = number
	# result: return keeper
	result = ''

	while i >= 0 and remain >= 0:
		# value is a number < base, representing a digit's value in base-10
		# hex: | A  | F  | 4  | 9  |
		# val: | 11 | 15 | 04 | 09 |
		value = math.floor(remain/base**(i))
		### print(f'@degree {i} value: {value*base**i}')
		# here we use value as an index to our GRAPHEMES constant to get our digit
		result += GRAPHEMES[value]
		### print(f'{result}')
		# next we reduce our remaining number by our value times its base to the ith power
		remain -= value*base**i
		# prepare i for next iteration
		i -= 1

	# make sure function didn't explode before returning
	assert remain == 0, f'function didn\'t return 0; returned {remain}'
	# return resulting string
	return result

def convert(digits, baseX, baseY):
	"""Convert given digits in baseX to digits in baseY.
	digits: str -- string representation of number (in baseX)
	baseX: int -- base of given number
	baseY: int -- base to convert to
	number10: int -- digits number in base 10
	return: str -- string representation of number (in baseY)"""
	#  Handle up to base 36 [0-9A-Z]
	assert 2 <= baseX <= 36, 'baseX is out of range: {}'.format(baseX)
	assert 2 <= baseY <= 36, 'baseY is out of range: {}'.format(baseY)
	number10 = decode(digits, baseX)
	return encode(number10, baseY)

def main():
	"""Read command-line arguments and convert given digits between bases."""
	import sys
	args = sys.argv[1:]  # Ignore script file name
	if len(args) == 3:
		digits = args[0]
		baseX = int(args[1])
		baseY = int(args[2])
		# Convert given digits between bases
		result = convert(digits, baseX, baseY)
		print('{} in base {} is {} in base {}'.format(digits, baseX, result, baseY))
	else:
		print('Usage: {} digits baseX baseY'.format(sys.argv[0]))
		print('Converts digits from baseX to baseY')


if __name__ == '__main__':
	main()
