#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
	"""A string of characters is a palindrome if it reads the same forwards and
	backwards, ignoring punctuation, whitespace, and letter casing."""
	# implement is_palindrome_iterative and is_palindrome_recursive below, then
	# change this to call your implementation to verify it passes all tests
	assert isinstance(text, str), 'input is not a string: {}'.format(text)
	return is_palindrome_iterative(text)
	# return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
	'''
	for each letter's index, check if [len-index-1] is equal
	if its not, then its not a palindrome
	'''

	length    = len(text) # used in several places
	iterator  = 0 # use an iterator for the while loop
	fudge_lft = 0 # these two values are declared just in case
	fudge_rgt = 0 # a non-alphanumeric character is skipped

	# lft and rgt are used to track indices
	# they need to be defined before the loop so we can check initially
	lft =            fudge_lft + iterator
	rgt =  length  - fudge_rgt - iterator - 1

	# loop through only half the text
	# if the string has an odd number of characters...
	# ...we don't need to compare the center value with itself
	while lft < length//2 and rgt >= length//2:

		lft =            fudge_lft + iterator
		rgt =  length  - fudge_rgt - iterator - 1

		# nesting these while loops still avoids O(n^2)
		# each time one of these while loops are hit...
		# ...the parent while loop is hit one less time
		while (not text[lft].isalpha()) and lft < rgt:
			# left index isn't alphabetical, so its skipped
			fudge_lft += 1
			lft = iterator + fudge_lft
		while (not text[rgt].isalpha()) and lft < rgt:
			# right index isn't alphabetical, so its skipped
			fudge_rgt += 1
			rgt =  length  - fudge_rgt - iterator - 1

		# finally, check if the letters are symmetrical
		if text[lft].lower() != text[rgt].lower():
			# this is not a palindrome
			return False
		else:
			# continue on loop
			iterator += 1

	else:
		# this is a palindrome
		return True


def is_palindrome_recursive(text, left=None, right=None):
	# TODO: implement the is_palindrome function recursively here
	pass

	# once implemented, change is_palindrome to call is_palindrome_recursive
	# to verify that your iterative implementation passes all tests


def main():
	import sys
	args = sys.argv[1:]  # Ignore script file name
	if len(args) > 0:
		for arg in args:
			is_pal = is_palindrome(arg)
			result = 'PASS' if is_pal else 'FAIL'
			is_str = 'is' if is_pal else 'is not'
			print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
	else:
		print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
		print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
	main()
