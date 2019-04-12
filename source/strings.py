#!python

def validate(text, pattern):
	assert isinstance(text, str), f'text is not a string: {text}'
	assert isinstance(pattern, str), f'pattern is not a string: {pattern}'


def contains(text, pattern):
	'''
	Return a boolean indicating whether pattern occurs in text.
	'''
	validate(text, pattern) # validate input
	# will iterate through a number of times equal to
	# len(BIG) - len(sml) + 1
	#-------------
	# I I I I I I
	# o o o
	#   o o o
	#     o o o
	#       o o o
	#         x x
	if pattern == '':
		return True
	ii = 0
	while ii < len(text) - len(pattern) + 1:
		jj = 0
		while pattern[jj] == text[ii+jj]:
			jj += 1
			if jj >= len(pattern):
				return True
		ii += 1
	else:
		return False


def find_index(text, pattern):
	'''
	Return the starting index of the first occurrence of pattern in text, or None if not found.
	'''
	validate(text, pattern) # validate input
	# will iterate through a number of times equal to
	# len(BIG) - len(sml) + 1
	#-------------
	# I I I I I I
	# o o o
	#   o o o
	#     o o o
	#       o o o
	#         x x
	if pattern == '':
		return 0
	text_index = 0
	while text_index < len(text) - len(pattern) + 1:
		patt_index = 0

		# start iterating the pattern
		# check if next pattern letter matches
		while pattern[patt_index] == text[text_index+patt_index]:
			patt_index += 1

			# reached end of pattern
			if patt_index >= len(pattern):
				return text_index
		text_index += 1
	else:
		return None


def find_all_indexes(text, pattern):
	'''
	Return a list of starting indexes of all occurrences of pattern in text, or an empty list if not found.
	'''
	# TODO: Implement find_all_indexes here (iteratively and/or recursively)
	validate(text, pattern) # validate input
	# will iterate through a number of times equal to
	# len(BIG) - len(sml) + 1
	#-------------
	# I I I I I I
	# o o o
	#   o o o
	#     o o o
	#       o o o
	#         x x
	found = []
	if pattern == '':
		found = list(range(0,len(text)))
		return found
	ii = 0
	while ii < len(text) - len(pattern) + 1:
		jj = 0
		while pattern[jj] == text[ii+jj]:
			jj += 1
			if jj >= len(pattern):
				found.append(ii)
				break
		ii += 1
	else:
		return found


def test_string_algorithms(text, pattern):
	found = contains(text, pattern)
	print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
	# TODO: Uncomment these lines after you implement find_index
	index = find_index(text, pattern)
	print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
	# TODO: Uncomment these lines after you implement find_all_indexes
	indexes = find_all_indexes(text, pattern)
	print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
	'''
	Read command-line arguments and test string searching algorithms.
	'''
	import sys
	args = sys.argv[1:]  # Ignore script file name
	if len(args) == 2:
		text = args[0]
		pattern = args[1]
		test_string_algorithms(text, pattern)
	else:
		script = sys.argv[0]
		print('Usage: {} text pattern'.format(script))
		print('Searches for occurrences of pattern in text')
		print("\nExample: {} 'abra cadabra' 'abra'".format(script))
		print("contains('abra cadabra', 'abra') => True")
		print("find_index('abra cadabra', 'abra') => 0")
		print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
	main()
