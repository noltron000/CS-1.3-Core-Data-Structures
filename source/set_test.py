#!python

import unittest
from set import Set

class SetTest(unittest.TestCase):
	def test_init(self):
		simple_array = [1,2,3,'a','b','c']
		set_one = Set()
		set_two = Set(simple_array)
		assert(set_one.table.keys() == [])
		# check that an item is in simple_array
		for item in set_two.table.keys():
			assert(item in simple_array)

	def test_empty(self):
		simple_array = [1,2,3,'a','b','c']
		set_one = Set(simple_array)
		# TODO come up with a test for this
		# this should always be an empty Set()

	def test_self(self):
		simple_array = [1,2,3,'a','b','c']
		set_one = Set(simple_array)
		# check that an item is in simple_array
		for item in set_one.table.keys():
			assert(item in simple_array)

	def test_union(self):
		array_one = [1,2,3,4,5,6]
		array_two = [4,5,6,7,8,9]
		array_out = [1,2,3,4,5,6,7,8,9]
		set_one = Set(array_one)
		set_two = Set(array_two)
		set_union = set_one.union(set_two)
		assert(set_union.table.keys() == array_out)

	def test_intersection(self):
		array_one = [1,2,3,4,5,6]
		array_two = [4,5,6,7,8,9]
		array_out = [4,5,6]
		set_one = Set(array_one)
		set_two = Set(array_two)
		set_intersection = set_one.intersection(set_two)
		assert(set_intersection.table.keys() == array_out)

	def test_complement(self):
		array_one = [1,2,3,4,5,6]
		array_two = [4,5,6,7,8,9]
		array_out = [1,2,3]
		set_one = Set(array_one)
		set_two = Set(array_two)
		set_complement = set_one.complement(set_two)
		assert(set_complement.table.keys() == array_out)

	def test_difference(self):
		array_one = [1,2,3,4,5,6]
		array_two = [4,5,6,7,8,9]
		array_out = [1,2,3,7,8,9]
		set_one = Set(array_one)
		set_two = Set(array_two)
		set_complement = set_one.complement(set_two)
		# check that an item is in array_out
		for item in set_complement.table.keys():
			assert(item in array_out)

if __name__ == '__main__':
	unittest.main()
