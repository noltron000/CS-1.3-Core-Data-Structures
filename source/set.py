#!python

from hasthable import HashTable

class Set(object):
	'''
	[NOTE] DOCSTRING
	'''

	def __init__(this, data=None):
		'''
		[NOTE] DOCSTRING
		'''
		# [TODO] COMPLETE
		this.size = 0
		this.table = HashTable()


	def contains(this, item):
		'''
		[NOTE] DOCSTRING
		'''
		# [TODO] COMPLETE
		pass


	def add(this, item):
		'''
		[NOTE] DOCSTRING
		'''
		# [TODO] COMPLETE
		pass


	def remove(this, item):
		'''
		[NOTE] DOCSTRING
		'''
		# [TODO] COMPLETE
		pass


	def is_subset(this, that):
		'''
		[NOTE] DOCSTRING
		'''
		# [TODO] COMPLETE
		pass


	def empty(this, that=None):
		'''
		∅;  //;  {}
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
		┗━━━━━━━━━┛
		'''
		# [TODO] COMPLETE
		pass


	def self(this, that=None):
		'''
		this
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
		┗━━━━━━━━━┛
		'''

	def union(this, that):
		'''
		this ∪ that
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
		┗━━━━━━━━━┛
		'''
		# [TODO] COMPLETE
		pass


	def intersection(this, that):
		'''
		this ∩ that
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
		┗━━━━━━━━━┛
		'''
		# [TODO] COMPLETE
		pass


	def complement(this, that):
		'''
		this \ that
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
		┗━━━━━━━━━┛
		'''
		# [TODO] COMPLETE
		pass

	def difference(this, that):
		'''
		this ∪ that - this ∩ that
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
		┗━━━━━━━━━┛
		'''
		# [TODO] COMPLETE
		pass
