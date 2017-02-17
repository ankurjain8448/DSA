class Graph(object):

	def __init__(self, nodes):
		"""
			nodes starts with 1, no 0 node is here !!! 
			Just to keep things a bit simple
		"""
		nodes = nodes+1
		self.graph = [0]*nodes
		self.nodes = nodes
		for i in xrange(nodes):
			self.graph[i] = []

	def add_edge(self, u, v):
		self.graph[u].append(v)

	def print_graph(self):
		print "========== GRAPH ============="
		for index, each_row in enumerate(self.graph):
			if index == 0:
				continue
			print each_row
		print "========== GRAPH END ============="

	@staticmethod
	def sample_data():
		return [[2,4], [1,],[1,2,],[1,3,5],[]]
