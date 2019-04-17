#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

	def __init__(self, iterable=None):
		'''
		Initialize this stack and push the given items, if any.
		'''
		# Initialize a new linked list to store the items
		self.list = LinkedList()
		if iterable is not None:
			for item in iterable:
				self.push(item)


	def __repr__(self):
		'''
		Return a string representation of this stack.
		'''
		return f'Stack({self.length()} items, top={self.peek()})'


	def is_empty(self):
		'''
		Return True if this stack is empty, or False otherwise.
		'''
		return self.length() == 0


	def length(self):
		'''
		Return the number of items in this stack.
		'''
		return self.list.size


	def push(self, item):
		'''
		Insert the given item on the top of this stack.
		Running time: O(1) – append just uses the HEAD pointer.
		'''
		self.list.append(item)


	def peek(self):
		'''
		Return the item on the top of this stack,
		w/out removing it, or None if this stack is empty.
		'''
		if self.list.tail == None:
			return None
		else:
			return self.list.tail.data


	def pop(self):
		'''
		Remove and return the item on the top of this stack,
		or raise ValueError if this stack is empty.
		Running time: O(n) - must change TAIL by iterating
		through the entire list, and pointing to it.
		'''
		if self.list.tail == None:
			raise ValueError("there's nothing to pop!")
		else: 
			node = self.list.tail
			# there's a case with repeated data where
			# this implementation could be concerning
			# it'd be better to remove from an index
			self.list.delete(node.data)
			return node.data


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

	def __init__(self, iterable=None):
		'''
		Initialize this stack and push the given items, if any.
		'''
		# Initialize a new list (dynamic array) to store the items
		self.list = list()
		if iterable is not None:
			for item in iterable:
				self.push(item)


	def __repr__(self):
		'''
		Return a string representation of this stack.
		'''
		return f'Stack({self.length()} items, top={self.peek()})'


	def is_empty(self):
		'''
		Return True if this stack is empty, or False otherwise.
		'''
		return self.length() == 0


	def length(self):
		'''
		Return the number of items in this stack.
		'''
		return len(self.list)


	def push(self, item):
		'''
		Insert the given item on the top of this stack.
		Running time: O(1) - append is constant time
		'''
		self.list.append(item)


	def peek(self):
		'''
		Return the item on the top of this stack without removing it,
		or None if this stack is empty.
		'''
		if len(self.list) == 0:
			return None
		else:
			return self.list[len(self.list) - 1]


	def pop(self):
		'''
		Remove and return the item on the top of this stack,
		or raise ValueError if this stack is empty.
		Running time: O(1) - the array doesn't shift at all.
		'''
		if len(self.list) == 0:
			raise ValueError("there's nothing to pop!")
		else:
			return self.list.pop()


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
