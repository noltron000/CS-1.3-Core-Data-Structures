#!python

def linear_search(array, item):
	'''
	return the first index of item in array or None if item is not found
	'''
	# implement linear_search_iterative and linear_search_recursive below, then
	# change this to call your implementation to verify it passes all tests
	# return linear_search_iterative(array, item)
	return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
	# loop over all array values until item is found
	for index, value in enumerate(array):
		if item == value:
			return index  # found
	return None  # not found


def linear_search_recursive(array, item, index=0):
	# try breaks nicely on errors
	try:
		# check if found
		if item == array[index]:
			return index # found
	# else redo function with index+1
		else:
			return linear_search_recursive(array, item, index+1)
		# except usually hits if array[index] doesn't exist
	except:
		return None # not found / error


def binary_search(array, item):
	'''
	return the index of item in sorted array or None if item is not found
	'''
	# implement binary_search_iterative and binary_search_recursive below, then
	# change this to call your implementation to verify it passes all tests
	return binary_search_iterative(array, item)
	# return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
	# declare left and right
	# rgt needs a {-1} because we count 0
	lft=0
	rgt=len(array) - 1

	while lft <= rgt:
		# mid is average of lft and rgt
		mid = (lft+rgt)//2

		# we can check if array@mid is a match
		if item == array[mid]:
			# found match
			return mid

		# alphabetically, is item larger?
		elif item > array[mid]:
			lft = mid + 1

		# alphabetically, is item smaller?
		elif item < array[mid]:
			rgt = mid - 1

	# item was not found
	return None


def binary_search_recursive(array, item):
	# TODO: improve comments, improve try statement, no more accidentally quadratic
	if len(array) > 0:
		half = len(array)//2
	else:
		return None

	# these print statements helped me figure out whats left and right
	### print("\n\n~~~Spit Data~~~")
	### print("     half: ",half)
	### print("  halfway: ",array[half])
	### print("    array: ",array)
	### print("     left: ",array[:half])
	### print("    right: ",array[half+1:])

	try:
		if item == array[half]:
			# found match
			return half

		elif item < array[half]:
			# alphabetically, item is smaller
			left_slice = array[:half]
			result = binary_search_recursive(left_slice, item)
			return result # notice there is no half+1 here

		elif item > array[half]:
			# alphabetically, item is larger
			right_slice = array[half+1:]
			result = binary_search_recursive(right_slice, item)
			return result + half + 1 # must add half+1 for right slices

	except:
		# break nicely
		return None
