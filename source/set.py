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


	def is_superset(self, other):
		'''
		checks if every item in other exists in self
		returns true or false
		'''
		for other_item in other.table:
			# check in case the item does not exist
			if not self.contains(other_item):
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
		# [FIXME] COMPLETE
		pass


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
		# self.table already records itself, return it
		return self.table

	def union(self, other):
		'''
		THE UNION OF TWO SETS
		contain all items appearing in either set
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
		# [FIXME] COMPLETE
		pass


	def intersection(self, other):
		'''
		THE INTERSECTION OF TWO SETS
		contain only items appearing in both sets
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
		# [FIXME] COMPLETE
		pass


	def complement(self, other):
		'''
		THE RELATIVE COMPLEMENT OF TWO SETS
		contain items from the 1st set that arent in the 2nd
		[NOTE] this is the only case where the order matters
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
		# [FIXME] COMPLETE
		pass


	def difference(self, other):
		'''
		THE SYMMETRIC DIFFERENCE OF TWO SETS
		contain items appearing in either set, but not both sets
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
		# [FIXME] COMPLETE
		pass
