#!python

from linkedlist import LinkedList


class HashTable(object):
	def __init__(self, init_size=8):
		'''
		Initialize this hash table with the given initial size.
		O(b) time where b is init_size
		'''
		self.buckets = [LinkedList() for i in range(init_size)]
		self.size = 0  # Number of key-value entries
		self.load_threshold = 0.75 # load factor threshold


	def __str__(self):
		'''
		Return a string representation of this hash table.
		'''
		items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
		return '{' + ', '.join(items) + '}'


	def __repr__(self):
		'''
		Return a string representation of this hash table.
		'''
		return 'HashTable({!r})'.format(self.items())


	def _bucket_index(self, key):
		'''
		Return the bucket index for the given key.
		'''
		return hash(key) % len(self.buckets)


	def load_factor(self):
		'''
		Return the load factor.
		(load factor: the ratio of number of entries to buckets)
		---
		Best and worst case running time:
		O(n) -> Division is a constant time operation
		length of self.buckets is O(n) though!
		'''
		return self.size / len(self.buckets)


	def keys(self):
		'''
		Return a list of all keys in this hash table.
		---
		Best and worst case running time:
		O(Items) -> this will run once per item (not bucket)
		'''
		# Collect all keys in each of the buckets
		all_keys = []
		for bucket in self.buckets:
			for key, value in bucket.items():
				all_keys.append(key)
		return all_keys


	def values(self):
		'''
		Return a list of all values in this hash table.
		---
		Best and worst case running time:
		O(Items) -> this will run once per item (not bucket)
		'''
		# Collect all values in each of the buckets
		all_values = []
		for bucket in self.buckets:
			for key, value in bucket.items():
				all_values.append(value)
		return all_values


	def items(self):
		'''
		Return a list of all entries in this hash table.
		(entries are key-value pairs)
		---
		Best and worst case running time:
		O(n) where n is total number of entries
		'''
		# Collect all pairs of key-value entries in each of the buckets
		all_items = []
		for bucket in self.buckets:
			all_items.extend(bucket.items())
		return all_items


	def length(self):
		'''
		Return the number of key-value entries by traversing its buckets.
		---
		Best and worst case running time: ??? under what conditions? [NOTE]
		'''
		# Count number of key-value entries in each of the buckets
		item_count = 0
		for bucket in self.buckets:
			item_count += bucket.length()
		return item_count
		# Equivalent to this list comprehension:
		return sum(bucket.length() for bucket in self.buckets)


	def contains(self, key):
		'''
		Return True if this hash table contains the given key, or False.
		---
		Best case running time: ??? under what conditions? [NOTE]
		---
		Worst case running time: ??? under what conditions? [NOTE]
		'''
		# Find the bucket the given key belongs in
		index = self._bucket_index(key)
		bucket = self.buckets[index]
		# Check if an entry with the given key exists in that bucket
		node = bucket.find(lambda key_value: key_value[0] == key)
		return node is not None  # True or False


	def get(self, key):
		'''
		Return the value associated with the given key, or raise KeyError.
		---
		Best case running time: ??? under what conditions? [NOTE]
		---
		Worst case running time: ??? under what conditions? [NOTE]
		'''
		# Find the bucket the given key belongs in
		index = self._bucket_index(key)
		bucket = self.buckets[index]
		# Find the node with the given key in that bucket, if one exists
		node = bucket.find(lambda key_value: key_value[0] == key)

		if node is not None: # Found
			# Get entry from node
			entry = node.data
			# Return the given key's associated value
			assert isinstance(entry, tuple)
			assert len(entry) == 2
			return entry[1]
		else:  # Not found
			raise KeyError(f'Key not found: {key}')


	def set(self, key, value):
		'''
		Insert or update the given key with its associated value.
		---
		Best case running time: ??? under what conditions? [NOTE]
		---
		Worst case running time: ??? under what conditions? [NOTE]
		'''
		# Find the bucket the given key belongs in
		index = self._bucket_index(key)
		bucket = self.buckets[index]

		# Check if an node with the given key exists in that bucket
		# Find the node with the given key in that bucket, if one exists
		node = bucket.find(lambda key_value: key_value[0] == key)

		if node is not None: # Found
			# Get entry from node
			entry = node.data
			# In this case, the given key's value is being updated
			# Remove the old key-value entry from the bucket first
			bucket.delete(entry)
		else:
			# Since node doesnt exist, we create a new one
			self.size += 1
		# Insert the new key-value entry into bucket either way
		bucket.append((key, value))

		# Check if the load factor exceeds a threshold
		if self.load_factor() > self.load_threshold:
			# Automatically resize to reduce the load factor
			self._resize()


	def delete(self, key):
		'''
		Delete the given key and its associated value, or raise KeyError.
		---
		Best case running time: ??? under what conditions? [NOTE]
		---
		Worst case running time: ??? under what conditions? [NOTE]
		'''
		# Find the bucket the given key belongs in
		index = self._bucket_index(key)
		bucket = self.buckets[index]

		# Find the node with the given key in that bucket, if one exists
		node = bucket.find(lambda key_value: key_value[0] == key)

		if node is not None: # Found
			# Get entry from node
			entry = node.data
			# Remove the key-value entry from the bucket
			bucket.delete(entry)
			# Reduce self.size
			self.size -= 1
		else:  # Not found
			raise KeyError(f'Key not found: {key}')


	def _resize(self, new_size=None):
		'''
		Resize this hash table's buckets and rehash all key-value entries.
		Should be called automatically when load factor exceeds a threshold
		such as 0.75 after an insertion (when set is called with a new key).
		---
		Best and worst case running time: ??? under what conditions? [NOTE]
		---
		Best and worst case space usage: ??? what uses this memory? [NOTE]
		'''
		# If unspecified, choose new size dynamically based on current size
		if new_size is None:
			new_size = len(self.buckets) * 2  # Double size
		# Option to reduce size if buckets are sparsely filled (low load factor)
		elif new_size is 0:
			new_size = len(self.buckets) / 2  # Half size

		# Get a list to temporarily hold all current key-value entries
		temp_entries = self.items()

		# Re-Initialize using an empty array with new_size
		self.__init__(new_size)

		for entry in temp_entries:
			key = entry[0]
			val = entry[1]
			self.set(key, val)


def test_hash_table():
	ht = HashTable(4)
	print('HashTable: ' + str(ht))

	print('Setting entries:')
	ht.set('I', 1)
	print('set(I, 1): ' + str(ht))
	ht.set('V', 5)
	print('set(V, 5): ' + str(ht))
	print('size: ' + str(ht.size))
	print('length: ' + str(ht.length()))
	print('buckets: ' + str(len(ht.buckets)))
	print('load_factor: ' + str(ht.load_factor()))
	ht.set('X', 10)
	print('set(X, 10): ' + str(ht))
	ht.set('L', 50)  # Should trigger resize
	print('set(L, 50): ' + str(ht))
	print('size: ' + str(ht.size))
	print('length: ' + str(ht.length()))
	print('buckets: ' + str(len(ht.buckets)))
	print('load_factor: ' + str(ht.load_factor()))

	print('Getting entries:')
	print('get(I): ' + str(ht.get('I')))
	print('get(V): ' + str(ht.get('V')))
	print('get(X): ' + str(ht.get('X')))
	print('get(L): ' + str(ht.get('L')))
	print('contains(X): ' + str(ht.contains('X')))
	print('contains(Z): ' + str(ht.contains('Z')))

	print('Deleting entries:')
	ht.delete('I')
	print('delete(I): ' + str(ht))
	ht.delete('V')
	print('delete(V): ' + str(ht))
	ht.delete('X')
	print('delete(X): ' + str(ht))
	ht.delete('L')
	print('delete(L): ' + str(ht))
	print('contains(X): ' + str(ht.contains('X')))
	print('size: ' + str(ht.size))
	print('length: ' + str(ht.length()))
	print('buckets: ' + str(len(ht.buckets)))
	print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
	test_hash_table()
