#!python

class BinaryTreeNode(object):
	def __init__(self, data):
		'''
		Initialize this binary tree node with the given data.
		'''
		self.data = data
		self.left = None
		self.right = None


	def __repr__(self):
		'''
		Return a sensible string representation of this Node.
		'''
		return 'BinaryTreeNode({!r})'.format(self.data)


	def is_leaf(self):
		'''
		Return True if this node is a leaf.
		A leaf has zero children.
		'''
		# check if neither left nor right child has a value
		return self.left is None and self.right is None


	def is_branch(self):
		'''
		Return True if this node is a branch.
		A branch has one or more children.
		'''
		# check if either left or right child have a value
		return self.left is not None or self.right is not None


	def height(self):
		'''
		Return the height of this node.
		The height of a node is the number of edges on the path
		to get to the lowest descendant leaf node possible.
		If this node itself is a leaf, it has a height of zero.
		The height of a non-existant node (NoneType) is zero.
		---
		best & worst case runtime: O(n)
		-> we must traverse every node to find the height.
		'''
		if self.is_leaf():
			return 0

		else:
			# does right child have a value?
			if self.left is not None:
				# if so, calculate its height
				left_height = self.left.height()
			else:
				left_height = 0

			# does right child have a value?
			if self.right is not None:
				# if so, calculate its height
				right_height = self.right.height()
			else:
				right_height = 0

			# retrieve the bigger of the two sides, and add one
			return max(left_height, right_height) + 1


class BinarySearchTree(object):

	def __init__(self, items=None):
		'''
		1. Initialize binary search tree.
		2. Insert given items.
		'''
		# initialize properties
		self.root = None
		self.size = 0

		# insert items
		if items is not None:
			for item in items:
				self.insert(item)


	def __repr__(self):
		'''
		Return a sensible string representation of this Tree.
		'''
		return f'BinarySearchTree({self.size} nodes)'


	def is_empty(self):
		'''
		Return True if this binary search tree is empty.
		An empty tree has no nodes.
		'''
		return self.root is None


	def height(self):
		'''
		Return the height of this tree.
		The height of a tree equals the height of the root node.
		---
		best & worst case runtime: O(n)
		--> we must traverse every node to find the height.
		'''
		return self.root.height()


	def contains(self, item):
		'''
		Does this binary search tree contain the given item?
		- Yes! Return True; the item is found.
		- No! Return False; the item is not found.
		* Note that search is eerily similar to contains.
		---
		best case runtime: O(1)
		--> the root node contains our item.
		---
		median case runtime: O(ln(n))
		--> the item is a leaf in a balanced tree.
		---
		worst case runtime: O(n)
		--> the tree can be represented using a linked list.
		    the item is at the tail of the linked list.
		'''
		# find a node with the given item, if any
		node = self._find_ITR(item, self.root)
		# return true if item was found...or false if not
		return node is not None


	def search(self, item):
		'''
		Does this binary search tree contain the given item?
		- Yes! Return our Node; here is our item's container.
		- No! Return None; the node for our item doesn't exist.
		* Note that search is eerily similar to contains.
		---
		best case runtime: O(1)
		--> the root node contains our item.
		---
		median case runtime: O(ln(n))
		--> the item is a leaf in a balanced tree.
		---
		worst case runtime: O(n)
		--> the tree can be represented using a linked list.
		    the item is at the tail of the linked list.
		'''
		# find a node with the given item, if any
		node = self._find_ITR(item, self.root)
		# return our node if item was found...or none if not
		if node is None:
			return None
		else:
			# HACK this is sort of done wierd.
			# I want this to return the entire node.
			return node.data


	def insert(self, item):
		'''
		Insert a given item into this tree.
		The tree must maintain a strict sorted structure.
		* Note the runtime is based on our search methods.
		---
		best case runtime: O(1)
		--> the root node is our parent node.
		---
		median case runtime: O(ln(n))
		--> our parent node is a leaf in a balanced tree.
		---
		worst case runtime: O(n)
		--> the tree can be represented using a linked list.
		    our parent node is at the tail of the linked list.
		'''
		# handle the case where the tree is empty
		if self.is_empty():
			# create a new root node with given item
			self.root = BinaryTreeNode(item)
			self.size += 1

		else:
			# find the parent node of our new item
			# this determines where the item should be inserted
			parent = self._find_parent_ITR(item, self.root)

			# should the item be inserted left of its parent?
			if item <= parent.data:
				# if so, set the parent's left child to a new node
				parent.left = BinaryTreeNode(item)
				self.size += 1

			# should the item be inserted right of its parent?
			elif item > parent.data :
				# if so, set the parent's right child to a new node
				parent.right =  BinaryTreeNode(item)
				self.size += 1


	"""
	def delete(self, item):
		'''
		Delete a selected item from this tree.
		The tree must maintain a strict sorted structure.
		---
		best case runtime: O(XXX)
		--> NOTE: input docstring
		~~~
		worst case runtime: O(XXX)
		--> NOTE: input docstring
		'''
		# NOTE: STRETCH CHALLENGE!
		# TODO: this function is based on the node's # children:
		# - 0 children (easiest)
		# - 1 child (medium)
		# - 2 children (most difficult)
		# to make this function, each case needs helper methods
		# the helper methods themselves could need more helpers
	"""


	def _find_RCR(self, item, node):
		'''
		Retrieve the node holding the given item in this tree.
		If the item is not found, return None.
		Search is used recursively, starting from given node.
		---
		best case runtime: O(1)
		--> the root node is our parent node.
		---
		median case runtime: O(ln(n))
		--> our parent node is a leaf in a balanced tree.
		---
		worst case runtime: O(n)
		--> the tree can be represented using a linked list.
		    our parent node is at the tail of the linked list.
		'''
		# check if starting node exists
		if node is None:
			# item not found (base case)
			return node

		# check if the given item matches the node's data
		elif item == node.data:
			# return the found node
			return node

		# is the given item smaller than the node's data?
		elif item < node.data:
			# recursively descend to the node's left children
			return self._find_RCR(item, node.left)

		# is the given item is bigger than the node's data?
		elif item > node.data:
			# recursively descend to the node's right children
			return self._find_RCR(item, node.right)


	def _find_parent_RCR(self, item, node, parent=None):
		'''
		Find the parent node of the node with the given item.
		This parent is where the given item would be inserted.
		If the tree has one or none nodes, there is no parent.
		The search is performed recursively from the given node.
		---
		best case runtime: O(1)
		--> the root node is our parent node.
		---
		median case runtime: O(ln(n))
		--> our parent node is a leaf in a balanced tree.
		---
		worst case runtime: O(n)
		--> the tree can be represented using a linked list.
		    our parent node is at the tail of the linked list.
		'''
		# check if starting node exists
		if node is None:
			# item not found (base case)
			# if there is no parent, this is NoneType
			return parent

		# check if the given item matches the node's data
		elif item == node.data:
			# return the parent of the found node
			return parent

		# is the given item smaller than the node's data?
		elif item <= node.data:
			# recursively descend to the node's left children
			return self._find_parent_RCR(item, node.left, node)

		# is the given item is bigger than the node's data?
		elif item > node.data:
			# recursively descend to the node's right children
			return self._find_parent_RCR(item, node.right, node)


	def _traverse_in_order_RCR(self, node, visit):
		'''
		This is a "Depth-First Search" algorithm.
		Traverse this binary tree recursively, in-order.
		To do so, visit the given node's left children.
		Visit the given node itself, then visit right children.
		---
		best & worst case runtime: O(n)
		--> we must traverse every node to visit them all
		~~~
		best & worst case memory usage: O(1)
		--> there is hardly any memory usage - its really 
		    contingent on whatever visit(node) does
		'''
		# traverse left subtree, if it exists
		if node.left is not None:
			self._traverse_in_order_RCR(node.left, visit)

		# visit this node's data with given function
		visit(node.data)

		# traverse right subtree, if it exists
		if node.right is not None:
			self._traverse_in_order_RCR(node.right, visit)


	def _traverse_pre_order_RCR(self, node, visit):
		'''
		This is a "Depth-First Search" algorithm.
		Traverse this binary tree recursively, pre-order.
		To do so, visit the given node.
		Then, visit it's left & right children.
		---
		best & worst case runtime: O(n)
		--> we must traverse every node to visit them all.
		~~~
		best & worst case memory usage: O(1)
		--> there is hardly any memory usage - its really 
		    contingent on whatever visit(node) does.
		--> note that, being recursive, it could be O(ln(n))
		    TODO ↑ this above statement is important, read into
		'''
		# visit this node's data with given function
		visit(node.data)

		# traverse left subtree, if it exists
		if node.left is not None:
			self._traverse_pre_order_RCR(node.left, visit)

		# traverse right subtree, if it exists
		if node.right is not None:
			self._traverse_pre_order_RCR(node.right, visit)


	def _traverse_post_order_RCR(self, node, visit):
		'''
		This is a "Depth-First Search" algorithm.
		Traverse this binary tree recursively, post-order.
		To do so, visit the given node's left & right children.
		Then, visit the given node itself
		---
		best & worst case runtime: O(n)
		--> we must traverse every node to visit them all.
		~~~
		best & worst case memory usage: O(1)
		--> there is hardly any memory usage - its really 
		    contingent on whatever visit(node) does
		'''
		# traverse left subtree, if it exists
		if node.left is not None:
			self._traverse_post_order_RCR(node.left, visit)

		# traverse right subtree, if it exists
		if node.right is not None:
			self._traverse_post_order_RCR(node.right, visit)

		# visit this node's data with given function
		visit(node.data)


	"""
	def _traverse_level_order_RCR(self):
		'''
		this method was not on the list.
		TODO why was it not on the list?
		'''
	"""


	def _find_ITR(self, item, node):
		'''
		Retrieve the node holding the given item in this tree.
		If the item is not found, return None.
		Search is used iteratively, starting from given node.
		---
		best case runtime: O(1)
		--> the root node is our parent node.
		---
		median case runtime: O(ln(n))
		--> our parent node is a leaf in a balanced tree.
		---
		worst case runtime: O(n)
		--> the tree can be represented using a linked list.
		    our parent node is at the tail of the linked list.
		'''
		# loop until node is none, a non-existant element
		while node is not None:

			# check if the given item matches the node's data
			if item == node.data:
				# return the found node
				return node

			# is the given item smaller than the node's data?
			elif item < node.data:
				# descend to the node's left child
				node = node.left

			# is the given item is bigger than the node's data?
			elif item > node.data:
				# descend to the node's right child
				node = node.right

		# expected node does not exist
		else:
			# item not found (base case)
			return node


	def _find_parent_ITR(self, item, node, parent=None):
		'''
		Find the parent node of the node with the given item.
		This parent is where the given item would be inserted.
		If the tree has one or none nodes, there is no parent.
		The search is performed iteratively from the given node.
		---
		best case runtime: O(1)
		--> the root node is our parent node.
		---
		median case runtime: O(ln(n))
		--> our parent node is a leaf in a balanced tree.
		---
		worst case runtime: O(n)
		--> the tree can be represented using a linked list.
		    our parent node is at the tail of the linked list.
		'''
		# loop until node is none, a non-existant element
		while node is not None:

			# check if the given item matches the node's data
			if item == node.data:
				# return the parent of the found node
				return parent

			# is the given item smaller than the node's data?
			elif item < node.data:
				# update the parent & descend to node's left child
				parent = node
				node = node.left

			# is the given item is bigger than the node's data?
			elif item > node.data:
				# update the parent & descend to node's right child
				parent = node
				node = node.right

		# expected node does not exist
		else:
			# item not found (base case)
			return parent


	"""
	def _traverse_in_order_ITR(self, node, visit):

		'''
		This is a "Depth-First Search" algorithm.
		Traverse this binary tree iteratively, in-order.
		To do so, visit the given node's left children.
		Visit the given node itself, then visit right children.
		---
		best & worst case runtime: O(n)
		--> we must traverse every node to visit them all
		~~~
		best & worst case memory usage: O(1)
		--> there is hardly any memory usage - its really 
		    contingent on whatever visit(node) does
		'''
		# NOTE: STRETCH CHALLENGE!
		# TODO: traverse in-order without using recursion
	"""


	"""
	def _traverse_pre_order_ITR(self, node, visit):
		'''
		This is a "Depth-First Search" algorithm.
		Traverse this binary tree iteratively, pre-order.
		To do so, visit the given node.
		Then, visit it's left & right children.
		---
		best & worst case runtime: O(n)
		--> we must traverse every node to visit them all.
		~~~
		best & worst case memory usage: O(1)
		--> there is hardly any memory usage - its really 
		    contingent on whatever visit(node) does
		'''
		# NOTE: STRETCH CHALLENGE!
		# TODO: traverse pre-order without using recursion
	"""


	"""
	def _traverse_post_order_ITR(self, node, visit):
		'''
		This is a "Depth-First Search" algorithm.
		Traverse this binary tree iteratively, post-order.
		To do so, visit the given node's left & right children.
		Then, visit the given node itself
		---
		best & worst case runtime: O(n)
		--> we must traverse every node to visit them all.
		~~~
		best & worst case memory usage: O(1)
		--> there is hardly any memory usage - its really 
		    contingent on whatever visit(node) does
		'''
		# NOTE: STRETCH CHALLENGE!
		# TODO: traverse post-order without using recursion
	"""


	def _traverse_level_order_ITR(self, start_node, visit):
		'''
		This is a "Breadth-First Search" algorithm
		Traverse this binary tree iteratively, level-order.
		This level-order style is like reading a paragraph,
		    reading each node on a level from left to right.
		To do implement this, we must use a queue.
		---
		best & worst case runtime: O(XXX)
		--> NOTE: input docstring
		~~~
		best & worst case memory usage: O(XXX)
		--> NOTE: input docstring
		'''
		# HACK: used an array over an actual queue.
		# this makes it slower than it should actually be.
		queue = [start_node]
		while queue != []:
			# dequeue node at front of queue
			node = queue.pop()
			# visit this node's data with given function
			visit(node.data)
			# enqueue this node's left child, if it exists
			if node.left:
				queue.insert(0, node.left)
			# enqueue this node's right child, if it exists
			if node.right:
				queue.insert(0, node.right)


	def items_in_order(self):
		'''
		Return an in-order list of all items in this tree.
		---
		best & worst case runtime: O(n)
		--> we must traverse every node to list them all
		~~~
		best & worst case memory usage: O(n)
		--> the hardest use of memory is tracking the array
		'''
		items = []
		if not self.is_empty():
			# traverse the tree in-order from the root node.
			# here, 'visit' appends nodes to the items array.
			function = items.append
			self._traverse_in_order_RCR(self.root, function)
		# return the in-order list of all items in tree
		return items


	def items_pre_order(self):
		'''
		Return a pre-order list of all items in this tree.
		---
		best & worst case runtime: O(n)
		--> we must traverse every node to list them all
		~~~
		best & worst case memory usage: O(n)
		--> the hardest use of memory is tracking the array
		'''
		items = []
		if not self.is_empty():
			# traverse the tree pre-order from the root node.
			# here, 'visit' appends nodes to the items array.
			function = items.append
			self._traverse_pre_order_RCR(self.root, function)
		# return the pre-order list of all items in tree
		return items


	def items_post_order(self):
		'''
		Returns a post-order list of all items in this tree.
		---
		best & worst case runtime: O(n)
		--> we must traverse every node to list them all
		~~~
		best & worst case memory usage: O(n)
		--> the hardest use of memory is tracking the array
		'''
		items = []
		if not self.is_empty():
			# traverse tree post-order from the root node.
			# here, 'visit' appends nodes to the items array.
			function = items.append
			self._traverse_post_order_RCR(self.root, function)
		# return post-order list of all items in tree
		return items


	def items_level_order(self):
		'''
		Return a level-order list of all items in this tree.
		'''
		items = []
		if not self.is_empty():
			# traverse tree level-order from the root node.
			# here, 'visit' appends nodes to the items array.
			function = items.append
			self._traverse_level_order_ITR(self.root, function)
		# return level-order list of all items in tree
		return items


def test_binary_search_tree():
	# create a binary search tree of n items in level-order
	short = [2, 1, 3]
	medium = [4, 2, 6, 1, 3, 5, 7]
	long = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]

	# select an array
	items = long
	print(f'items: {items}')

	tree = BinarySearchTree()
	print(f'tree: {tree}')
	print(f'root: {tree.root}')

	print('\nInserting items:')
	for item in items:
		tree.insert(item)
		print(f'insert({item}), size: {tree.size}')
	print(f'root: {tree.root}')

	print('\nSearching for items:')
	for item in items:
		result = tree.search(item)
		print(f'search({item}): {result}')
	item = 123
	result = tree.search(item)
	print(f'search({item}): {result}')

	print('\nTraversing items:')
	print(f'items in-order:    {tree.items_in_order()}')
	print(f'items pre-order:   {tree.items_pre_order()}')
	print(f'items post-order:  {tree.items_post_order()}')
	print(f'items level-order: {tree.items_level_order()}')


if __name__ == '__main__':
	test_binary_search_tree()
