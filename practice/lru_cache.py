class Node(object):
	"""docstring for Node"""
	def __init__(self, value):
		self.freq = value
		self.next = None
		self.items = set()

class Linklist(object):
	def __init__(self):
		self.head = None
		self.last = None

	def insert(self):
		node = Node(1)
		if self.head is None:
			self.head = node
			self.last = self.head
		else:
			last_node = self.last
			node.freq = last_node.freq + 1
			last_node.next = node
			self.last = last_node.next
		return

	def remove_current_node(self, current_node):
		ptr1 = current_node.next
		temp = self.head
		ptr = None
		while temp:
			if temp == current_node:
				break
			ptr = temp
			temp = temp.next
		del current_node

	def insert_at_head(self):
		if self.head:
			temp = self.head
			new_node = Node(1)
			new_node.next = temp
			self.head = new_node
		else:
			self.insert()

	def remove_empty_nodes(self):
		# traverse using back_edge
		temp = self.head
		while temp:
			next = temp.next
			if temp.items:
				self.head = temp
				break
			else:
				self.remove_current_node(temp)
			temp = next

	def create_new_node(self, previous_node, value):
		# need to take care of this
		if previous_node.next :
			# previous_node is not last node
			temp = previous_node.next
			new_node = Node(value)
			new_node.next = previous_node.next
			previous_node.next = new_node
		else:
			# previous_node is last node
			self.insert()

	def delete(self, value):
		temp = self.head
		if temp.value == value:
			self.head = self.head.next
			return 
		ptr = None
		while temp :
			if temp.value == value:
				ptr.next = temp.next
				break
			ptr = temp
			temp = temp.next
		return

	def traverse(self):
		temp = self.head
		while temp:
			print temp.value
			temp = temp.next
		return


class LRU(object):
	"""LRU cache implemetation"""
	def __init__(self, cache_size):
		'''
			LinkedHaspMap
		'''
		super(LRU, self).__init__()
		self.cache_size = cache_size
		self.current_cache_size = 0
		self.linklist = Linklist()
		self.hash_map = {} # (key, linklist node{node contains freq and items})

	def print_cache(self):
		temp = self.linklist.head
		while temp:
			print "{} {}".format(temp.freq, temp.items)
			temp = temp.next

	def insert(self, key):
		'''
			insert the key
		'''
		if key in self.hash_map:
			self.delete(key)
			self.insert(key)
		else:
			if self.current_cache_size < self.cache_size:
				if self.linklist.head is None or self.linklist.head.freq != 1:
					self.linklist.insert_at_head()
				self.hash_map[key] = self.linklist.head
				self.linklist.head.items.add(key)
			else:
				if not self.linklist.head.items:
					# remove empty nodes
					self.linklist.remove_empty_nodes()
				item_to_remove = self.linklist.head.items.pop()
				del self.hash_map[item_to_remove]
				self.current_cache_size -= 1
				self.insert(key)
			self.current_cache_size += 1
		print "current_cache_size : ", self.current_cache_size
		# self.print_cache()


	def delete(self, key):
		'''
			delete the key
		'''
		node = self.hash_map.get(key, None)
		if node:
			del self.hash_map[key]
			node.items.remove(key)
			self.current_cache_size -= 1
		else:
			print "key : {} is not present".format(key)
		# self.print_cache()


	def get(self, key):
		'''
			update the key
			increment the frequency count
		'''
		node = self.hash_map.get(key, None)
		if node:
			if node.next is None:
				self.linklist.create_new_node(node, node.freq + 1)
			if node.freq + 1 == node.next.freq:
				self.hash_map[key] = node.next
				node.items.remove(key)
				node.next.items.add(key)
			else:
				self.linklist.create_new_node(node, node.freq + 1)
				self.get(key)
		else:
			print "key : {} is not present".format(key)
		# self.print_cache()

print """Enter e/E to exit \n 
i : Insert
d : delete
g : get
EX :

  i <value>
  d <value>
  g <value>

"""

cache_size = 5
cache = LRU(cache_size)
mapper = {'i' : cache.insert, 'g' : cache.get , 'd': cache.delete, 'p': cache.print_cache}
while True :
	op = raw_input("Enter operation and value \n").strip().split()
	if op[0] in ['e', "E"]:
		break
	if op[0] == 'p':
		mapper[op[0]]()
	else:
		mapper[op[0]](op[1])
