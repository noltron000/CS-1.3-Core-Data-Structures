#!python

from hashtable import HashTable


class Set(object):
	def __init__(self, data=None):
		'''
		[TODO] DOCSTRING
		'''
		# [FIXME] COMPLETE
		this.size = 0
		this.table = HashTable()



	def contains(self, item):
		'''
		[TODO] DOCSTRING
		'''
		# [FIXME] COMPLETE
		pass


	def add(self, item):
		'''
		[TODO] DOCSTRING
		'''
		# [FIXME] COMPLETE
		pass


	def remove(self, item):
		'''
		[TODO] DOCSTRING
		'''
		# [FIXME] COMPLETE
		pass


	def is_subset(self, other):
		'''
		[TODO] DOCSTRING
		'''
		# [FIXME] COMPLETE
		pass


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
		┗━━━━━━━━━┛ = this
		'''
		# [FIXME] COMPLETE
		pass


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
		┗━━━━━━━━━┛ = this ∪ that
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
		┗━━━━━━━━━┛ = this ∩ that
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
		┗━━━━━━━━━┛ = this \ that
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
		┗━━━━━━━━━┛ = this ∪ that - this ∩ that
		'''
		# [FIXME] COMPLETE
		pass
