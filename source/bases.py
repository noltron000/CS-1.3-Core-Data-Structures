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
GRAPHEMES = string.digits + string.ascii_uppercase

def decode(digits, base):
	"""Decode given digits in given base to number in base 10.
	digits: str -- string representation of number (in given base)
	base: int -- base of given number
	return: int -- integer representation of number (in base 10)"""
	# Handle up to base 36 [0-9A-Z]
	assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
	# TODO: Encode number in any base

def encode(number, base):
	"""Encode given number in base 10 to digits in given base.
	number: int -- integer representation of number (in base 10)
	base: int -- base to convert to
	return: str -- string representation of number (in given base)"""
	# Handle up to base 36 [0-9A-Z]
	print(f'\n---encode function--- num:{number} base:{base}')
	assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
	# Handle unsigned numbers only for now
	assert number >= 0, 'number is negative: {}'.format(number)
	# TODO: Encode number in any base

	# 36 -> 100
	# Find out first n where (base**degree > number)
	# n+1 turns out to be number of digits needed
	degree = 0
	while base**degree <= number:
		print(f'@ degree {degree}: {base**degree} is less than or equal to {number}')
		degree += 1
	print(f'@ degree {degree}: {base**degree} is more than {number}')
	print(f'There are {degree} base-{base} digits the answer\n')

	result = ''
	remain = number
	# degree iterator
	iter_deg = degree

	while iter_deg > 0 and remain > 0:
		# dimension is the base-10 number equivalent for the specific nth place
		# essentially if we had a base 16 number, each digit is a dimension, expressed in base-10
		# hex: A  F  4  9
		# dim: 11 15 04 09
		dimension = math.floor(remain/base**(iter_deg-1))
		# graphemes are available characters - output finds correct character mapping to base-10 number
		output = GRAPHEMES[dimension]
		result += output
		remain -= dimension*(base**(iter_deg-1))
		iter_deg -= 1
	print(result)



def convert(digits, baseX, baseY):
	"""Convert given digits in baseX to digits in baseY.
	digits: str -- string representation of number (in baseX)
	baseX: int -- base of given number
	baseY: int -- base to convert to
	number10: int -- digits number in base 10
	return: str -- string representation of number (in baseY)"""
	# Handle up to base 36 [0-9A-Z]
	assert 2 <= baseX <= 36, 'baseX is out of range: {}'.format(baseX)
	assert 2 <= baseY <= 36, 'baseY is out of range: {}'.format(baseY)
	number10 = decode(digits, baseX)
	# return encode(number10, baseY)
	return encode(33, baseY)

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
