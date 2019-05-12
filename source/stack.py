#!python

from linkedlist import LinkedList

class LinkedStack(object):
# assignment details:
# 1. implement LinkedStack.
# 2. change the variable at the bottom to use this stack.
# 3. verify it passes all tests.

	def __init__(self, iterable=None):
		'''
		Initialize this stack and push the given items, if any.
		'''
		# make a new LinkedList.
		self.list = LinkedList()

		# add iterable items, if they exist.
		if iterable:
			for item in iterable:
				self.push(item)


	def __repr__(self):
		'''
		Return a string representation of this stack.
		'''
		return f'Stack(count={self.length()} top={self.peek()})'


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
		---
		Running time: O(1)
		--> push just uses the HEAD pointer.
		'''
		self.list.append(item)


	def peek(self):
		'''
		Return the item on top of this stack. Don't remove it!
		If the stack is empty, return None instead.
		'''
		if self.list.tail == None:
			return None
		else:
			return self.list.tail.data


	def pop(self):
		'''
		Return the item on top of this stack, and remove it.
		If the stack is empty, raise ValueError instead.
		---
		Running time: O(n)
		--> must change TAIL by iterating through entire list,
		    and then pointing two it.
		'''
		if self.list.tail == None:
			raise ValueError("there's nothing to pop!")
		else: 
			node = self.list.tail
			# HACK:
			# there's a case with repeated data where
			# this implementation could be concerning
			# it'd be better to remove from an index
			self.list.delete(node.data)
			return node.data


class ArrayStack(object):
# assignment details:
# 1. implement ArrayStack.
# 2. change the variable at the bottom to use this stack.
# 3. verify it passes all tests.
	def __init__(self, iterable=None):
		'''
		Initialize this stack and push the given items, if any.
		'''
		# initialize a new list (dynamic array) to store items.
		self.list = list()
		
		# add iterable items, if they exist.
		if iterable is not None:
			for item in iterable:
				self.push(item)


	def __repr__(self):
		'''
		Return a string representation of this stack.
		'''
		return f'Stack(count={self.length()} top={self.peek()})'


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
		---
		Running time: O(1)
		--> append is constant time
		'''
		self.list.append(item)


	def peek(self):
		'''
		Return the item on top of this stack. Don't remove it!
		If the stack is empty, return None instead.
		'''
		if len(self.list) == 0:
			return None
		else:
			return self.list[len(self.list) - 1]


	def pop(self):
		'''
		Return the item on top of this stack, and remove it.
		If the stack is empty, raise ValueError instead.
		---
		Running time: O(1)
		--> the array doesn't shift at all.
		'''
		if len(self.list) == 0:
			raise ValueError("there's nothing to pop!")
		else:
			return self.list.pop()


# NOTE: you can switch export between the two Stack types.
# they both do the same thing in different ways.
# choose the prefered one by commenting out a single item:
Stack = LinkedStack
# Stack = ArrayStack
