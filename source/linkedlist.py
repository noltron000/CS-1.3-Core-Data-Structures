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
		Initialize this linked list and append the given items, if any.
		'''
		self.head = None  # First node
		self.tail = None  # Last node
		self.size = 0  # Number of nodes
		# Append the given items
		if iterable is not None:
			for item in iterable:
				self.append(item)


	def __str__(self):
		'''
		Return a formatted string representation of this linked list.
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
		for n items in the list because we always need to loop through all n nodes.
		'''
		# Create an empty list of results
		result = []  # Constant time to create a new list
		# Start at the head node
		node = self.head  # Constant time to assign a variable reference
		# Loop until the node is None, which is one node too far past the tail
		while node is not None:  # Always n iterations because no early exit
			# Append this node's data to the results list
			result.append(node.data)  # Constant time to append to a list
			# Skip to the next node
			node = node.next  # Constant time to reassign a variable
		# Now result contains the data from all nodes
		return result  # Constant time to return a list


	def is_empty(self):
		'''
		Return True if this linked list is empty, or False.
		'''
		return self.head is None


	def length(self):
		'''
		Return the length of this linked list by traversing its nodes.
		---
		Best & worst case run time: O(n) [todo] <Θ theta?>
		for n items in the list because we always need to loop through all n nodes
		'''
		# Node counter initialized to zero
		node_count = 0
		# Start at the head node
		node = self.head
		# Loop until the node is None, which is one node too far past the tail
		while node is not None:
			# Count one for this node
			node_count += 1
			# Skip to the next node
			node = node.next
		# Now node_count contains the number of nodes
		return node_count


	def get_at_index(self, index):
		'''
		Return the item at the given index in this linked list, or
		raise ValueError if the given index is out of range of the list size.
		---
		Best case run time: O(1) [todo] <Ω omega?>
		if item is near the head of the list or is not present.
		---
		Worst case run time: O(n)
		if item is near the tail of the list.
		'''
		# Check if the given index is out of range and if so raise an error
		if not (0 <= index < self.size):
			raise ValueError(f'List index out of range: {index}')

		# Index counter initialized to zero
		index_count = 0
		# Start at the head node
		node = self.head
		# Loop until the node is None or index item is found
		while True:
			# Check if condition is met
			if index_count == index:
				# Will always eventually get here
				print("\nFOUND NODE:",node)
				print("HEAD:",self.head)
				print("TAIL:",self.tail)
				return node
			# Count one for this node
			index_count += 1
			# Skip to the next node
			node = node.next


	def insert_at_index(self, index, item):
		'''
		Insert the given item at the given index in this linked list, or
		raise ValueError if the given index is out of range of the list size.
		---
		Best case run time: O() under what conditions? [TODO]
		---
		Worst case run time: O() under what conditions? [TODO]
		'''
		# Check if the given index is out of range and if so raise an error
		if not (0 <= index <= self.size):
			raise ValueError(f'List index out of range: {index}')

		# Check if index is head or tail
		if index == 0:
			return self.prepend(item)
		elif index == self.size:
			return self.append(item)

		# Get all our important nodes laid out
		prv_node = self.get_at_index(index - 1)
		new_node = Node(item)
		nxt_node = prv_node.next

		# Change some pointers around
		new_node.next = nxt_node
		prv_node.next = new_node

		# Finally, update size
		self.size += 1

	def append(self, item):
		'''
		Insert the given item at the tail of this linked list.
		---
		Best & worst case run time: O(1)
		Reading the tail or head is blazing fast. The other features in here are constant too.
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
		Reading the tail or head is blazing fast. The other features in here are constant too.
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


	def find_quality(self, quality):
		'''
		Return an item's data from this linked list satisfying the given quality function.
		---
		Best case run time: Ω(1) <omega>
		if item is near the head of the list.
		---
		Worst case run time: O(n)
		if item is near the tail of the list or not present
		and we need to loop through all n nodes in the list.
		'''
		# Start at the head node
		node = self.head  # Constant time to assign a variable reference
		# Loop until the node is None, which is one node too far past the tail
		while node is not None:  # Up to n iterations if we don't exit early
			# Check if this node's data satisfies the given quality function
			if quality(node.data):  # Constant time to call quality function
				# We found data satisfying the quality function, so exit early
				return node.data  # Constant time to return data
			# Skip to the next node
			node = node.next  # Constant time to reassign a variable
		# We never found data satisfying quality, but have to return something
		return None  # Constant time to return None


	def find_node(self, data):
		'''
		This function was copied from above and modified.
		Return a node whose data matches the given data parameter.
		---
		Best case run time: Ω(1) <omega>
		if item is near the head of the list.
		---
		Worst case run time: O(n)
		if item is near the tail of the list or not present
		and we need to loop through all n nodes in the list.
		'''
		# Start at the head node
		node = self.head  # Constant time to assign a variable reference
		# Loop until the node is None, which is one node too far past the tail
		while node is not None:  # Up to n iterations if we don't exit early
			# Check if this node's data satisfies the given data param
			if node.data == data:
				# We found matching data, so exit early
				return node
			# Skip to the next node
			node = node.next  # Constant time to reassign a variable
		# We never found data satisfying quality, but have to return something
		return None  # Constant time to return None


	def replace(self, old_item, new_item):
		'''
		Replace the given old_item in this linked list with given new_item
		using the same node, or raise ValueError if old_item is not found.
		---
		Best case run time: Ω(1) <omega>
		if item is near the head of the list.
		---
		Worst case run time: O(n)
		if item is near the tail of the list or not present
		and we need to loop through all n nodes in the list.
		---
		These run times are exactly the same as the called function it uses.
		'''
		# used find function to find node
		node = self.find_node(old_item)

		# Check if the node was not found
		if node == None:
			raise ValueError(f'Target node was not found: {node}')

		# changed nodes data with new data
		node.data = new_item


	def delete(self, item):
		'''
		Delete the given item from this linked list, or raise ValueError.
		---
		Best case run time: O(1)
		item is at the head.
		---
		Worst case run time: O(n)
		item is at the tail.
		'''
		# Start at the head node
		node = self.head
		# Keep track of the node before the one containing the given item
		previous = None
		# Create a flag to track if we have found the given item
		found = False
		# Loop until we have found the given item or the node is None
		while not found and node is not None:
			# Check if the node's data matches the given item
			if node.data == item:
				# We found data matching the given item, so update found flag
				found = True
			else:
				# Skip to the next node
				previous = node
				node = node.next
		# Check if we found the given item or we never did and reached the tail
		if found:
			# Check if we found a node in the middle of this linked list
			if node is not self.head and node is not self.tail:
				# Update the previous node to skip around the found node
				previous.next = node.next
				# Unlink the found node from its next node
				node.next = None
			# Check if we found a node at the head
			if node is self.head:
				# Update head to the next node
				self.head = node.next
				# Unlink the found node from the next node
				node.next = None
			# Check if we found a node at the tail
			if node is self.tail:
				# Check if there is a node before the found node
				if previous is not None:
					# Unlink the previous node from the found node
					previous.next = None
				# Update tail to the previous node regardless
				self.tail = previous
			# Finally, update size
			self.size -= 1
		else:
			# Otherwise raise an error to tell the user that delete has failed
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
