#!python



def is_palindrome(text):
	"""A string of characters is a palindrome if it reads the same forwards and
	backwards, ignoring punctuation, whitespace, and letter casing."""
	# implement is_palindrome_iterative and is_palindrome_recursive below, then
	# change this to call your implementation to verify it passes all tests
	assert isinstance(text, str), 'input is not a string: {}'.format(text)
	# return is_palindrome_iterative(text)
	return is_palindrome_recursive(text)



def is_palindrome_iterative(text):
	'''
	for each letter's index, check if [len-index-1] is equal
	if its not, then its not a palindrome
	'''

	# lft & rgt represent index locations in the text
	# lft character index mirrors rgt character index
	lft = 0
	rgt = len(text) - 1

	# we go through the string at both ends,
	# checking if its mirrored along the way
	while lft < rgt:

		# these while loops will skip non-alphabetical chars
		# also, if lft==rgt, text[lft]==text[rgt], hence lft<rgt
		while not text[lft].isalpha() and lft < rgt:
			lft += 1
		while not text[rgt].isalpha() and lft < rgt:
			rgt -= 1

		# nesting these while loops still avoids O(n^2)
		# each time one of these while loops are hit...
		# ...the parent while loop is hit one less time

		# check if the letters are (not) symmetrical
		if text[lft].lower() != text[rgt].lower():
			return False
		else:
			# continue loop
			lft += 1
			rgt -= 1
	else:
		# if loop ends, this is a palindrome
		return True



def is_palindrome_recursive(text, lft=None, rgt=None):
	'''
	for each letter's index, check if [len-index-1] is equal
	if its not, then its not a palindrome
	'''

	# these can only be true on first run
	if lft == None:
		lft = 0
	if rgt == None:
		rgt = len(text) - 1
	if text == '':
		return True

	# we go through the string at both ends,
	# checking if its mirrored along the way
	while lft < rgt and not text[lft].isalpha():
		lft += 1
	while lft < rgt and not text[rgt].isalpha():
		rgt -= 1
	# check if the letters are symmetrical
	if text[lft].lower() != text[rgt].lower():
		return False
	elif lft >= rgt:
		return True
	else:
		# continue loop
		lft += 1
		rgt -= 1
		return is_palindrome_recursive(text,lft,rgt)



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
