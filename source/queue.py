#!python

from linkedlist import LinkedList

# assignment details:
# 1. implement LinkedQueue.
# 2. change the variable at the bottom to use this queue.
# 3. verify it passes all tests.

class LinkedQueue(object):
	def __init__(self, iterable=None):
		'''
		Initialize this queue and enqueue any given items.
		'''
		# make a new LinkedList.
		self.list = LinkedList()

		# add iterable items, if they exist.
		if iterable is not None:
			for item in iterable:
				self.enqueue(item)


	def __repr__(self):
		'''
		Return a string representation of this queue.
		'''
		return f'Queue({self.length()} items, front={self.front()})'


	def is_empty(self):
		'''
		Return True if this queue is empty, or False otherwise.
		'''
		return self.length() == 0


	def length(self):
		'''
		Return the number of items in this queue.
		'''
		return self.list.size


	def enqueue(self, item):
		'''
		Insert the given item at the back of this queue.
		Running time: O(1) – uses TAIL pointer
		Also, linkedlists do not track their index number,
		so the indices don't need to be updated.
		'''
		self.list.append(item)


	def front(self):
		'''
		Return the item at the front of this queue without removing it,
		or None if this queue is empty.
		'''
		if self.list.head == None:
			return None
		else:
			return self.list.head.data


	def dequeue(self):
		'''
		Remove and return the item at the front of this queue,
		or raise ValueError if this queue is empty.
		---
		Best case run time: O(1)
		--> item is at the head.
		    same as delete method.
		---
		Worst case run time: O(n)
		--> item is at the tail.
		    same as delete method.
		'''
		if self.list.head == None:
			raise ValueError("there's nothing to pop!")
		else: 
			node = self.list.head
			self.list.delete(node.data)
			return node.data

# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):
	def __init__(self, iterable=None):
		'''
		Initialize this queue and enqueue the given items, if any.
		'''
		# Initialize a new list (dynamic array) to store the items
		self.list = list()
		if iterable is not None:
			for item in iterable:
				self.enqueue(item)


	def __repr__(self):
		'''
		Return a string representation of this queue.
		'''
		return f'Queue({self.length()} items, front={self.front()})'


	def is_empty(self):
		'''
		Return True if this queue is empty, or False otherwise.
		'''
		return self.length() == 0


	def length(self):
		'''
		Return the number of items in this queue.
		'''
		return len(self.list)


	def enqueue(self, item):
		'''
		Insert the given item at the back of this queue.
		Running time: O(n) - Must shift every index down by one.
		'''
		# insert item at location 0, aka prepend
		self.list.insert(0, item)


	def front(self):
		'''
		Return the item at the front of the queue,
		w/out removing it, or None if this queue is empty.
		'''
		if len(self.list) == 0:
			return None
		else:
			return self.list[len(self.list) - 1]


	def dequeue(self):
		'''
		Remove and return the item at the front of this queue,
		or raise ValueError if this queue is empty.
		Running time: O(1)
		'''
		if len(self.list) == 0:
			raise ValueError("there's nothing to pop!")
		else:
			return self.list.pop()

# NOTE: you can switch export between the two Queue types.
# they both do the same thing in different ways.
# choose the prefered one by commenting out a single item:
Queue = LinkedQueue
# Queue = ArrayQueue
