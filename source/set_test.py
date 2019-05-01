#!python

import unittest
from set import Set
from hashtable import HashTable

class SetTest(unittest.TestCase):
	def test_init(self):
		simple_array = [1,2,3,'a','b','c']

		set_one = Set()
		set_two = Set(simple_array)
		assert(set_one.table.keys() == [])
		set_two.table.keys()

if __name__ == '__main__':
	unittest.main()
