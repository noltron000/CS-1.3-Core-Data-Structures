#!python

import math
# math is needed for floor operations
import string
# string.digits is '0123456789'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

GRAPHEMES = string.digits + string.ascii_letters
# google says: "a GRAPHEME is the smallest meaningful contrastive unit in a writing system"
# consider changing variable name to LEXICON
# here, it represents an alphanumeric digit in a base system larger than 10
# for example, a base-N system uses a digit of GRAPHEMES[N], although GRAPHEMES[N+1] would be invalid
# EX=9; print(f'{GRAPHEMES}\n' + ' '*EX + f'{GRAPHEMES[EX]}') # ← uncomment this line for an example



def decode(digits, base):
	'''
	Decode given digits in given base to number in base 10.
	-   base: int → base of given number
	- digits: str → string representation of number (in given base)
	- return: int → integer representation of number (in base 10)
	'''

	assert 2 <= base <= 36, f'base is out of range: {base}'
	# handle up to base 36 [0-9A-Z]
	digits = "".join(reversed(digits))
	# digits need to be reversed to properly loop through
	# numbers read right to left; strings and arrays read left to right
	result = 0
	# result stores updated return value
	degree = len(digits) - 1
	# degree is our iterator; it determines the power of our base in the loop

	while degree >= 0:
		mult = base**degree
		# mult converts whatever 1, 10, 100, ..., 10^degree is in base-b to base-10
		# for example, in base-10, 10 is 10^1, 100 is 10^2, and 1000 is 10^3
		# for example, in base-16, 10 is 16^1, 100 is 16^2, and 1000 is 16^3
		place = digits[degree]
		# place finds the nth-place of the digits string
		# for example, the 0th-place of 7a059f is 7
		# for example, the 4th-place of 7a059f is 9
		value = GRAPHEMES.index(place)*mult
		# value is a number < base, representing a digit's value in base-10
		# we find what a character means numerically by finding its index location in GRAPHEMES
		# list.index(x) finds y where list[y] = x
		# for example, convert a character to base-10:
		# hex: | A  | F  | 4  | 9  |
		# val: | 11 | 15 | 04 | 09 |
		result += value
		# keep track of the total sum, at the end of the loop it will be the total
		degree -= 1
		# keep track of the degree iterator
	return result



def encode(number, base):
	'''
	Encode given number in base 10 to digits in given base.
	-   base: int → base to convert to
	- number: int → integer representation of number (in base 10)
	- return: str → string representation of number (in given base)
	'''

	assert 2 <= base <= 36, f'base is out of range: {base}'
	# handle up to base 36 [0-9A-Z]
	assert number >= 0, f'number is negative: {number}'
	# handle unsigned numbers only for now
	degree = 0
	# degree represents the number of digits necessary in base-n
	# degree starts at 0; the first loop will determine its value

	while base**degree <= number:
	# this while loop finds the first base^power that is greater than the number given
	# this also happens to represent the number of digits needed for the base-b digit
		degree += 1
		# uncomment ↓↓↓ these ↓↓↓ print statements to better understand the loop
		### print(f'@degree {degree-1}: {base**(degree-1)} is less than or equal to {number}')
	### print(f'@degree {degree}: {base**degree} is more than {number}')
	### print(f'There are {degree} base-{base} digits the answer\n')

	remain = number
	# remain stores the remaining amount
	# remain should always end equal to 0
	result = ''
	# result stores updated return value
	degree -= 1
	# degree is currently the first degree at which base^degree is > number
	# degree is also our iterator; it determines the power of our base in the loop
	# for our loop, we need the last base^degree which is >= number; so we subtract one

	while degree >= 0 and remain >= 0:
	# degree is our iterator; it determines the power of our base in the loop
		value = math.floor(remain/base**(degree))
		# value is a number < base, representing a digit's value in base-10
		# hex: | A  | F  | 4  | 9  |
		# val: | 11 | 15 | 04 | 09 |
		result += GRAPHEMES[value]
		### print(f'@degree {i} value: {value*base**i}')
		# here we use value as an index to our GRAPHEMES constant to get our digit
		remain -= value*base**degree
		### print(f'{result}')
		# next we reduce our remaining number by our value times its base to the ith power
		degree -= 1
		# prepare degree for next iteration

	assert remain == 0, f'function didn\'t return 0; returned {remain}'
	# make sure function didn't explode before returning
	return result
	# return resulting string



def convert(digits, baseX, baseY):
	'''
	Convert given digits in baseX to digits in baseY
	-  baseX: int -- base of given number
	-  baseY: int -- base to convert to
	- digits: str -- string representation of number (in baseX)
	- return: str -- string representation of number (in baseY)
	'''

	assert 2 <= baseX <= 36, f'baseX is out of range: {baseX}'
	assert 2 <= baseY <= 36, f'baseY is out of range: {baseY}'
	# handle up to base 36 [0-9A-Z]
	value10 = decode(digits, baseX)
	# value10 is the decoded base-10 value of digits
	return encode(value10, baseY)
	# encode value10 into valueY and return



def main():
	'''
	Entrypoint when ran from the command-line.
	- reads command-line arguments (expects three)
	- convert given digits between bases
	'''
	import sys
	args = sys.argv[1:]
	# args ignores script file name
	if len(args) == 3:
		digits = args[0]
		baseX = int(args[1]) # old base
		baseY = int(args[2]) # new base
		result = convert(digits, baseX, baseY)
		# result is the digit converted between bases
		print(f'{digits} in base {baseX} is {result} in base {baseY}')
	else:
		print(f'Usage: \n$ {sys.argv[0]} digits baseX baseY\nConverts digits from baseX to baseY')



if __name__ == '__main__':
	main()
