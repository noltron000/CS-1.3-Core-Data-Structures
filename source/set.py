#!python



from hashtable import HashTable



class Set(object):
	def __init__(self, data=None):
		'''
		[TODO] DOCSTRING
		'''
		self.size = 0
		# self.table param should only be used where necessary;
		# enables hotswapping HashTable with another structure
		self.table = HashTable()

		# add data, if it is given
		if data:
			for item in data:
				self.add(item)



	def contains(self, item):
		'''
		verify whether an item exists in our set
		returns true or false
		'''
		# table.contains hashes a key and looks for it
		# in this case, our key is also the value we have
		return self.table.contains(item) # our item is the key



	def add(self, item):
		'''
		adds an item to our set
		unless it already exists
		'''
		# a set is a collection of well defined, unique objects
		# therefore, a set cannot hold duplicate items
		if not self.contains(item):
			# usually a hashtable has key-value pairs
			# notice how there is no value in our table.set()
			# table.set() assumes the value is none, if not given
			self.table.set(item) # item is a key, not a value
			self.size += 1



	def remove(self, item):
		'''
		removes an item from our set
		unless it does not exist
		'''
		# the set must contain the item before it can be removed
		if self.contains(item):
			self.table.delete(item)
			self.size -= 1



	def is_subset(self, other):
		'''
		checks if every item in other exists in self
		returns true or false
		[NOTE] this is a special case where the order matters
		'''
		for item in self.table.keys():
			# check in case the item does not exist
			if not other.contains(item):
				return False
		# for loop has ended successfully
		return True



	def empty(self, other=None):
		'''
		THE EMPTY SET
		will always return the empty set
		symbols include ∅, //, and {}
		┏━━━━━━━━━┓
		┃         ┃
		┃ ┌───┐   ┃
		┃ │   │   ┃
		┃ │ ┌─┼─┐ ┃
		┃ │ │ │ │ ┃
		┃ └─┼─┘ │ ┃
		┃   │   │ ┃
		┃   └───┘ ┃
		┃         ┃
		┗━━━━━━━━━┛ = ∅
		'''
		# [FIXME] COMPLETE BY ADDING COMMENTS
		return Set()



	def self(self, other=None):
		'''
		THE SELF SET
		will always return itself
		┏━━━━━━━━━┓
		┃         ┃
		┃ ┌───┐   ┃
		┃ │███│   ┃
		┃ │█┌─┼─┐ ┃
		┃ │█│█│ │ ┃
		┃ └─┼─┘ │ ┃
		┃   │   │ ┃
		┃   └───┘ ┃
		┃         ┃
		┗━━━━━━━━━┛ = self
		'''
		# [FIXME] COMPLETE BY ADDING COMMENTS
		return self



	def union(self, other):
		'''
		THE UNION OF TWO SETS
		contains all items appearing in either set
		┏━━━━━━━━━┓
		┃         ┃
		┃ ┌───┐   ┃
		┃ │███│   ┃
		┃ │█┌─┼─┐ ┃
		┃ │█│█│█│ ┃
		┃ └─┼─┘█│ ┃
		┃   │███│ ┃
		┃   └───┘ ┃
		┃         ┃
		┗━━━━━━━━━┛ = self ∪ other
		'''
		# [FIXME] COMPLETE BY ADDING COMMENTS
		output = Set()

		for item in self.table.keys():
			output.add(item)
		for item in other.table.keys():
			output.add(item)
		return output



	def intersection(self, other):
		'''
		THE INTERSECTION OF TWO SETS
		contains only items appearing in both sets
		┏━━━━━━━━━┓
		┃         ┃
		┃ ┌───┐   ┃
		┃ │   │   ┃
		┃ │ ┌─┼─┐ ┃
		┃ │ │█│ │ ┃
		┃ └─┼─┘ │ ┃
		┃   │   │ ┃
		┃   └───┘ ┃
		┃         ┃
		┗━━━━━━━━━┛ = self ∩ other
		'''
		# [FIXME] COMPLETE BY ADDING COMMENTS
		output = Set()
		for item in self.table.keys():
			# check if the item exists
			if other.contains(item):
				output.add(item)
		return output



	def complement(self, other):
		'''
		THE RELATIVE COMPLEMENT OF TWO SETS
		contains items from the 1st set that arent in the 2nd
		[NOTE] this is a special case where the order matters
		┏━━━━━━━━━┓
		┃         ┃
		┃ ┌───┐   ┃
		┃ │███│   ┃
		┃ │█┌─┼─┐ ┃
		┃ │█│ │ │ ┃
		┃ └─┼─┘ │ ┃
		┃   │   │ ┃
		┃   └───┘ ┃
		┃         ┃
		┗━━━━━━━━━┛ = self \ other
		'''
		# [FIXME] COMPLETE BY ADDING COMMENTS
		output = Set()
		for item in self.table.keys():
			# check if the item exists
			if not other.contains(item):
				output.add(item)
		return output



	def difference(self, other):
		'''
		THE SYMMETRIC DIFFERENCE OF TWO SETS
		contains items appearing in either set, but not both
		┏━━━━━━━━━┓
		┃         ┃
		┃ ┌───┐   ┃
		┃ │███│   ┃
		┃ │█┌─┼─┐ ┃
		┃ │█│ │█│ ┃
		┃ └─┼─┘█│ ┃
		┃   │███│ ┃
		┃   └───┘ ┃
		┃         ┃
		┗━━━━━━━━━┛ = self ∪ other - self ∩ other
		'''
		# [FIXME] COMPLETE BY ADDING COMMENTS
		output = Set()
		for item in self.complement(other).table.keys():
			output.add(item)
		for item in other.complement(self).table.keys():
			output.add(item)
		return output



def mini_test():
	my_set = Set([1,2,3])
	your_set = Set([2,3,4])

	print(my_set.table)
	print(your_set.table)

	new_set = my_set.union(your_set)
	print(new_set.table)

	new_set = my_set.intersection(your_set)
	print(new_set.table)

	new_set = my_set.complement(your_set)
	print(new_set.table)

	new_set = my_set.difference(your_set)
	print(new_set.table)



if __name__ == '__main__':
	mini_test()
