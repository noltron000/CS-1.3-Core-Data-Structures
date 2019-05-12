#!python


class Node(object):
	def __init__(self, data):
		'''
		Initialize this node with the given data.
		'''
		self.data = data
		self.next = None


	def __repr__(self):
		'''
		Return a string representation of this node.
		'''
		return f'Node({self.data})'


class LinkedList(object):
	def __init__(self, iterable=None):
		'''
		Initialize this linked list.
		Append given items, if any.
		'''
		self.head = None # First node
		self.tail = None # Last node
		self.size = 0 # Number of nodes
		# Append the given items
		if iterable is not None:
			for item in iterable:
				self.append(item)


	def __str__(self):
		'''
		Return a prettified string visualization.
		It will represent our linked list.
		'''
		items = [f'({item})' for item in self.items()]
		return f'[{" -> ".join(items)}]'


	def __repr__(self):
		'''
		Return a string representation of this linked list.
		'''
		return f'LinkedList({self.items()})'


	def items(self):
		'''
		Return a list of all items in this linked list.
		---
		Best & worst case run time: Θ(n) <theta>
		--> to get a list of all items, 
		    we must always visit all n items.
		'''
		# create an empty list of results.
		result = []
		# start at the head node.
		node = self.head
		# loop until the node is None,
		# which is one node too far past the tail.
		while node is not None:  # always O(n); no early exit.
			# append this node's data to the results list.
			result.append(node.data)
			# get the next node.
			node = node.next
		# now result contains the data from all nodes.
		return result # Constant time to return a list.


	def is_empty(self):
		'''
		Return True if this linked list is empty, or False.
		'''
		return self.head is None


	def length(self):
		'''
		Return the length of this linked list.
		This is done by traversing its nodes.
		---
		Best & worst case run time: O(n) [TODO] <Θ theta?>
		--> to get the length of our linked list,
		    we must always visit all n items.
		'''
		# node counter initialized to zero.
		node_count = 0
		# start at the head node.
		node = self.head
		# loop until the node is None,
		# which is one node too far past the tail.
		while node is not None:
			# count one for this node.
			node_count += 1
			# get the next node.
			node = node.next
		# now result contains the number of nodes.
		return node_count


	def get_at_index(self, index):
		'''
		Return the item at the given index in this linked list.
		Raise ValueError if the given index is out of range.
		---
		Best case run time: O(1) [TODO] <Ω omega?>
		if item is near the head of the list or is not present.
		---
		Worst case run time: O(n)
		if item is near the tail of the list.
		'''
		# check if the given index is out of range;
		# this only happens if index is negative or is massive.
		if not (0 <= index < self.size):
			raise ValueError(f'List index out of range: {index}')

		# index counter initialized to zero.
		index_count = 0
		# start at the head node.
		node = self.head

		# loop until the node is None or index item is found.
		# note that this while loop will never be false.
		while (0 <= index_count < self.size):
			# check if condition is met.
			if index_count == index:
				# will always eventually get here.
				return node
			# count one for this node.
			index_count += 1
			# skip to the next node.
			node = node.next

		else:
			raise ValueError('While loop broke unexpectedly.')


	def insert_at_index(self, index, item):
		'''
		Insert the given item at the given index in linked list.
		Raise ValueError if the given index is out of range.
		---
		Best case run time: O(1)
		--> method is fastest in one of two cases cases:
		    1. index is at the head
		    2. index is not present
		---
		Worst case run time: O(n)
		--> method is slowest if item is at the end of the list,
		    because it must loop through all n items to find it.
		'''
		# check if the given index is out of range;
		# this only happens if index is negative or is massive.
		if not (0 <= index <= self.size):
			raise ValueError(f'List index out of range: {index}')

		# check if index is head or tail.
		elif index == 0:
			self.prepend(item)
		elif index == self.size:
			self.append(item)

		# index is in the center of the list.
		else:
			# get all our important nodes laid out.
			prv_node = self.get_at_index(index - 1)
			nxt_node = prv_node.next
			new_node = Node(item)

			# change some pointers around.
			new_node.next = nxt_node
			prv_node.next = new_node

			# finally, update linked list size.
			self.size += 1


	def append(self, item):
		'''
		Insert the given item at the tail of this linked list.
		---
		Best & worst case run time: O(1)
		--> reading the tail or head is blazing fast.
		    the other features in here are constant too.
		'''
		# Create a new node to hold the given item
		new_node = Node(item)
		# Check if this linked list is empty
		if self.is_empty():
			# Assign head to new node
			self.head = new_node
		else:
			# Otherwise insert new node after tail
			self.tail.next = new_node
		# Update tail to new node regardless
		self.tail = new_node
		# Finally, update size
		self.size += 1


	def prepend(self, item):
		'''
		Insert the given item at the head of this linked list.
		---
		Best & worst case run time: O(1)
		--> reading the tail or head is blazing fast.
		    the other features in here are constant too.
		'''
		# Create a new node to hold the given item
		new_node = Node(item)
		# Check if this linked list is empty
		if self.is_empty():
			# Assign tail to new node
			self.tail = new_node
		else:
			# Otherwise insert new node before head
			new_node.next = self.head
		# Update head to new node regardless
		self.head = new_node
		# Finally, update size
		self.size += 1


	def find(self, quality):
		'''
		Search for some data in our linked list.
		Do this by using a 'quality' function;
		it returns a boolean - true if it is satisfied.
		Once found, return the node which encapsulates the data.
		---
		Best case run time: Ω(1) <omega>
		--> if item is near the head of the list.
		---
		Worst case run time: O(n)
		--> if item is near the tail of the list or not present
		    and we need to loop through all n nodes in the list.
		'''
		# start at the head node.
		node = self.head
		# loop until the node is None,
		# which is one node too far past the tail.
		while node is not None:  # O(n) w/ potential early exit.
			# does node's data satisfy the quality function?
			if quality(node.data):
				# quality function is satisfied, return the node.
				# note that we exit early when we find a match.
				return node
			# otherwise skip to the next node.
			node = node.next
		# quality function was never satisfied...
		# meaning there is no matching node that exists to find!
		return None


	def replace(self, old_data, new_data):
		'''
		Find the a node with the given old_data.
		Update it to contain the given new_data.
		Raise ValueError if old_data is not found.
		---
		Best case run time: Ω(1) <omega>
		--> same as the find method
		---
		Worst case run time: O(n)
		--> same as the find method
		'''
		# used find method to find node.
		node = self.find(lambda item: item == old_data)

		# check if the node was not found.
		if node == None:
			raise ValueError(f'Target node was not found: {node}')

		# changed node's data with new data.
		node.data = new_data


	def delete(self, item):
		'''
		Delete the given item from this linked list.
		If for some reason we can't, raise ValueError.
		TODO: refactor using find() function.
		---
		Best case run time: O(1)
		--> item is at the head.
		---
		Worst case run time: O(n)
		--> item is at the tail.
		'''
		# start at the head node.
		node = self.head
		# keep track of the previous node.
		# do this since the list is not doubly-linked.
		prv_node = None
		# create a flag to track if we have found the given item.
		found = False
		# loop until we find the given item, or reach the tail.
		# if the node is None, we have reached the tail.
		while not found and node is not None:
			# check if the node's data matches the given item.
			if node.data == item:
				# we found data matching the given item.
				found = True
			else:
				# skip to the next node.
				prv_node = node
				node = node.next
		# check if we found the given item or not.
		if found:
			# check if we found a node in the middle of this list.
			if node is not self.head and node is not self.tail:
				# update prv_node to skip around the found node.
				prv_node.next = node.next
				# unlink the found node from its next node.
				node.next = None
			# check if we found a node at the head.
			if node is self.head:
				# update head to the next node.
				self.head = node.next
				# unlink the found node from the next node.
				node.next = None
			# check if we found a node at the tail.
			if node is self.tail:
				# check if there is a node before the found node.
				if prv_node is not None:
					# unlink the prv_node from the found node.
					prv_node.next = None
				# update tail to the prv_node regardless.
				self.tail = prv_node
			# finally, update size.
			self.size -= 1
		else:
			raise ValueError(f'Item not found: {item}')


def test_linked_list():
	ll = LinkedList()
	print(ll)

	print('Appending items:')
	ll.append('A')
	print(ll)
	ll.append('B')
	print(ll)
	ll.append('C')
	print(ll)
	print(f'head: {ll.head}')
	print(f'tail: {ll.tail}')
	print(f'size: {ll.size}')
	print(f'length: {ll.length()}')

	print('Getting items by index:')
	for index in range(ll.size):
		item = ll.get_at_index(index).data
		print(f'get_at_index({index}): {item}')

	print('Deleting items:')
	ll.delete('B')
	print(ll)
	ll.delete('C')
	print(ll)
	ll.delete('A')
	print(ll)
	print(f'head: {ll.head}')
	print(f'tail: {ll.tail}')
	print(f'size: {ll.size}')
	print(f'length: {ll.length()}')


if __name__ == '__main__':
	test_linked_list()
