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
		# check if both left child and right child have no value
		return self.left is None and self.right is None

	def is_branch(self):
		'''
		Return True if this node is a branch.
		A branch has one or more children.
		'''
		# check if either left child or right child has a value
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
		node = self._find_recursive(item, self.root)
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
		node = self._find_recursive(item, self.root)
		# return our node if item was found...or none if not
		return node

	def insert(self, item):
		'''
		Insert the given item in order into this binary search tree.
		TODO: Best case running time: ??? under what conditions?
		TODO: Worst case running time: ??? under what conditions?
		'''
		# Handle the case where the tree is empty
		if self.is_empty():
			# TODO: Create a new root node
			self.root = ...
			# TODO: Increase the tree size
			self.size ...
			return
		# Find the parent node of where the given item should be inserted
		parent = self._find_parent_node_recursive(item, self.root)
		# TODO: Check if the given item should be inserted left of parent node
		if ...:
			# TODO: Create a new node and set the parent's left child
			parent.left = ...
		# TODO: Check if the given item should be inserted right of parent node
		elif ...:
			# TODO: Create a new node and set the parent's right child
			parent.right = ...
		# TODO: Increase the tree size
		self.size ...

	def _find_iterative(self, item):
		'''
		Return the node containing the given item in this binary search tree,
		or None if the given item is not found. Search is performed iteratively
		starting from the root node.
		TODO: Best case running time: ??? under what conditions?
		TODO: Worst case running time: ??? under what conditions?
		'''
		# Start with the root node
		node = self.root
		# Loop until we descend past the closest leaf node
		while node is not None:
			# TODO: Check if the given item matches the node's data
			if ...:
				# Return the found node
				return node
			# TODO: Check if the given item is less than the node's data
			elif ...:
				# TODO: Descend to the node's left child
				node = ...
			# TODO: Check if the given item is greater than the node's data
			elif ...:
				# TODO: Descend to the node's right child
				node = ...
		# Not found
		return None

	def _find_recursive(self, item, node):
		'''
		Return the node containing the given item in this binary search tree,
		or None if the given item is not found. Search is performed recursively
		starting from the given node (give the root node to start recursion).
		TODO: Best case running time: ??? under what conditions?
		TODO: Worst case running time: ??? under what conditions?
		'''
		# Check if starting node exists
		if node is None:
			# Not found (base case)
			return None
		# TODO: Check if the given item matches the node's data
		elif ...:
			# Return the found node
			return node
		# TODO: Check if the given item is less than the node's data
		elif ...:
			# TODO: Recursively descend to the node's left child, if it exists
			return ...
		# TODO: Check if the given item is greater than the node's data
		elif ...:
			# TODO: Recursively descend to the node's right child, if it exists
			return ...

	def _find_parent_node_iterative(self, item):
		'''
		Return the parent node of the node containing the given item
		(or the parent node of where the given item would be if inserted)
		in this tree, or None if this tree is empty or has only a root node.
		Search is performed iteratively starting from the root node.
		TODO: Best case running time: ??? under what conditions?
		TODO: Worst case running time: ??? under what conditions?
		'''
		# Start with the root node and keep track of its parent
		node = self.root
		parent = None
		# Loop until we descend past the closest leaf node
		while node is not None:
			# TODO: Check if the given item matches the node's data
			if ...:
				# Return the parent of the found node
				return parent
			# TODO: Check if the given item is less than the node's data
			elif ...:
				# TODO: Update the parent and descend to the node's left child
				parent = ...
				node = ...
			# TODO: Check if the given item is greater than the node's data
			elif ...:
				# TODO: Update the parent and descend to the node's right child
				parent = ...
				node = ...
		# Not found
		return parent

	def _find_parent_node_recursive(self, item, node, parent=None):
		'''
		Return the parent node of the node containing the given item
		(or the parent node of where the given item would be if inserted)
		in this tree, or None if this tree is empty or has only a root node.
		Search is performed recursively starting from the given node
		(give the root node to start recursion).
		'''
		# Check if starting node exists
		if node is None:
			# Not found (base case)
			return None
		# TODO: Check if the given item matches the node's data
		if ...:
			# Return the parent of the found node
			return parent
		# TODO: Check if the given item is less than the node's data
		elif ...:
			# TODO: Recursively descend to the node's left child, if it exists
			return ...  # Hint: Remember to update the parent parameter
		# TODO: Check if the given item is greater than the node's data
		elif ...:
			# TODO: Recursively descend to the node's right child, if it exists
			return ...  # Hint: Remember to update the parent parameter

	def delete(self, item):
		'''
		Remove given item from this tree, if present, or raise ValueError.
		TODO: Best case running time: ??? under what conditions?
		TODO: Worst case running time: ??? under what conditions?
		'''
		# TODO: Use helper methods and break this algorithm down into 3 cases
		# based on how many children the node containing the given item has and
		# implement new helper methods for subtasks of the more complex cases

	def items_in_order(self):
		'''
		Return an in-order list of all items in this binary search tree.
		'''
		items = []
		if not self.is_empty():
			# Traverse tree in-order from root, appending each node's item
			self._traverse_in_order_recursive(self.root, items.append)
		# Return in-order list of all items in tree
		return items

	def _traverse_in_order_recursive(self, node, visit):
		'''
		Traverse this binary tree with recursive in-order traversal (DFS).
		Start at the given node and visit each node with the given function.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
		'''
		# TODO: Traverse left subtree, if it exists
		# ...
		# TODO: Visit this node's data with given function
		# ...
		# TODO: Traverse right subtree, if it exists
		# ...

	def _traverse_in_order_iterative(self, node, visit):
		'''
		Traverse this binary tree with iterative in-order traversal (DFS).
		Start at the given node and visit each node with the given function.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
		'''
		# TODO: Traverse in-order without using recursion (stretch challenge)

	def items_pre_order(self):
		'''
		Return a pre-order list of all items in this binary search tree.
		'''
		items = []
		if not self.is_empty():
			# Traverse tree pre-order from root, appending each node's item
			self._traverse_pre_order_recursive(self.root, items.append)
		# Return pre-order list of all items in tree
		return items

	def _traverse_pre_order_recursive(self, node, visit):
		'''
		Traverse this binary tree with recursive pre-order traversal (DFS).
		Start at the given node and visit each node with the given function.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
		'''
		# TODO: Visit this node's data with given function
		# ...
		# TODO: Traverse left subtree, if it exists
		# ...
		# TODO: Traverse right subtree, if it exists
		# ...

	def _traverse_pre_order_iterative(self, node, visit):
		'''
		Traverse this binary tree with iterative pre-order traversal (DFS).
		Start at the given node and visit each node with the given function.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
		'''
		# TODO: Traverse pre-order without using recursion (stretch challenge)

	def items_post_order(self):
		'''
		Return a post-order list of all items in this binary search tree.
		'''
		items = []
		if not self.is_empty():
			# Traverse tree post-order from root, appending each node's item
			self._traverse_post_order_recursive(self.root, items.append)
		# Return post-order list of all items in tree
		return items

	def _traverse_post_order_recursive(self, node, visit):
		'''
		Traverse this binary tree with recursive post-order traversal (DFS).
		Start at the given node and visit each node with the given function.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
		'''
		# TODO: Traverse left subtree, if it exists
		# ...
		# TODO: Traverse right subtree, if it exists
		# ...
		# TODO: Visit this node's data with given function
		# ...

	def _traverse_post_order_iterative(self, node, visit):
		'''
		Traverse this binary tree with iterative post-order traversal (DFS).
		Start at the given node and visit each node with the given function.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
		'''
		# TODO: Traverse post-order without using recursion (stretch challenge)

	def items_level_order(self):
		'''
		Return a level-order list of all items in this binary search tree.
		'''
		items = []
		if not self.is_empty():
			# Traverse tree level-order from root, appending each node's item
			self._traverse_level_order_iterative(self.root, items.append)
		# Return level-order list of all items in tree
		return items

	def _traverse_level_order_iterative(self, start_node, visit):
		'''
		Traverse this binary tree with iterative level-order traversal (BFS).
		Start at the given node and visit each node with the given function.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
		'''
		# TODO: Create queue to store nodes not yet traversed in level-order
		queue = ...
		# TODO: Enqueue given starting node
		# ...
		# TODO: Loop until queue is empty
		while ...:
			# TODO: Dequeue node at front of queue
			node = ...
			# TODO: Visit this node's data with given function
			# ...
			# TODO: Enqueue this node's left child, if it exists
			# ...
			# TODO: Enqueue this node's right child, if it exists
			# ...


def test_binary_search_tree():
	# Create a complete binary search tree of 3, 7, or 15 items in level-order
	# items = [2, 1, 3]
	items = [4, 2, 6, 1, 3, 5, 7]
	# items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
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
# recommended mnemonic (& synonym list)
# TODO
# FIXME
# XXX
# BUG (BUGFIX)
# HACK (CLEVER, MAGIC)
# NOTE (HELP)

if __name__ == '__main__':
	test_binary_search_tree()
