class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.next = None
		

class SingleLinklist(object):
	def __init__(self):
		self.head = None
		self.start = None
		self.current = None

	def add_node(self, node):
		node = Node(node)
		if self.head:
			self.current.next = node
			self.current = self.current.next
		else:
			self.head = node
			self.current = self.head
		return self.head

	def print_linklist(self):
		temp = self.head
		while temp:
			print temp.val
			temp = temp.next


if __name__ == '__main__':
	ll = SingleLinklist()
	nodes = 10
	for i in xrange(10):
		ll.add_node(i)
	ll.print_linklist()
