#!python

def validate(text, pattern):
	assert isinstance(text, str), f'text is not a string: {text}'
	assert isinstance(pattern, str), f'pattern isnt a string: {pattern}'


def _search(
	text,  # text is a string input
	pattern,  # pattern is a string to find within text
	case_empty, # the case where the pattern is nothing
	case_match, # the case where the pattern matches
	case_false, # the case where the pattern doesn't match
	break_flag # a flag to break or return in the loop
):
	'''
	best-case runtime: O(1)
	--> this can be just O(1) under a few cases.
	    case 1) the pattern is an empty string.
	    case 2) the pattern is one character long,
	    and is found at the beginning of the given text.
			case 3) the text string itself is empty.
	--- 
	worst-case runtime: O(n^2)
	--> the worst case happens in a very specific situation.
	    imagine you have a pattern, 'aaaaab'.
	    imagine you have a text,    'aaaaaaaaab'.
	    the program will have to loop through all n
	    characters of the pattern a total of N-n times;
	    where N is the length of the text. 
	    O(n*(N-n)) ≈ O(n^2)
	~~~
	best-case memory usage: O(XXX)
	---
	worst-case memory usage: O(XXX)
	'''
	# will iterate through a number of times equal to
	# len(BIG) - len(sml) + 1
	#-------------
	# I I I I I I
	# o o o
	#   o o o
	#     o o o
	#       o o o
	#         x x
	validate(text, pattern) # validate input
	if pattern == '':
		return case_empty()
	ii = 0
	while ii < len(text) - len(pattern) + 1:
		jj = 0
		while pattern[jj] == text[ii+jj]:
			jj += 1
			if jj >= len(pattern):
				if not break_flag:
					return case_match(ii)
				case_match(ii)
				break
		ii += 1
	else:
		return case_false()


def contains(text, pattern):
	'''
	the time complexity of this is contingent on _search().
	here, it is essentially the same as _search().
	'''
	case_empty = lambda x=None: True
	case_match = lambda x=None: True
	case_false = lambda x=None: False
	break_flag = False
	return _search(
		text,
		pattern,
		case_empty,
		case_match,
		case_false,
		break_flag
	)


def find_index(text, pattern):
	'''
	the time complexity of this is contingent on _search().
	here, it is essentially the same as _search().
	'''
	case_empty = lambda x=None: 0
	case_match = lambda x=None: x
	case_false = lambda x=None: None
	break_flag = False
	return _search(
		text,
		pattern,
		case_empty,
		case_match,
		case_false,
		break_flag
	)


def find_all_indexes(text, pattern):
	'''
	the time complexity of this is contingent on _search().
	here, it is essentially the same as _search().
	note that it will often be O(n) rather than O(1), though.
	to find all indices, we have to loop over the entire text.
	the exception is with an empty string; best-case is O(1).
	'''
	found = []
	case_empty = lambda x=None: list(range(0,len(text)))
	case_match = lambda x=None: found.append(x)
	case_false = lambda x=None: found
	break_flag = True
	return _search(
		text,
		pattern,
		case_empty,
		case_match,
		case_false,
		break_flag
	)


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
		print(f'Usage: {script} text pattern')
		print('Searches for occurrences of pattern in text')
		print(f"\nExample: {script} 'abra cadabra' 'abra'")
		print("contains('abra cadabra', 'abra') => True")
		print("find_index('abra cadabra', 'abra') => 0")
		print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
	main()
