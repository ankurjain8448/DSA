class Graph(object):
	def __init__(self, nodes):
		nodes = nodes+1
		self.graph = [0]*nodes
		self.nodes = nodes
		for i in xrange(nodes):
			self.graph[i] = []

	def add_edge(self, u, v):
		self.graph[u].append(v)

	def dfs(self, start_node):
		self.visited = [False]*self.nodes
		self.dfs_recursive(start_node)

	def dfs_recursive(self, start_node):
		"""
			Don't call me directly # call dfs
		"""
		# print ">> dfs for : ", start_node
		if not self.visited[start_node]:
			self.visited[start_node] = True
			print "visited : ", start_node
			for each_node in self.graph[start_node]:
				self.dfs_recursive(each_node)
		# else:
		# 	print "already visited : ", start_node

	def print_graph(self):
		print "========== GRAPH ============="
		for index, each_row in enumerate(self.graph):
			if index == 0:
				continue
			print each_row
		print "========== GRAPH END ============="


if __name__ == '__main__':
	Input = [
	[2,4],
	[1,],
	[1,2,],
	[4,1,3],
	]
	nodes = len(Input)
	g = Graph(nodes)
	u = 0
	for _ in Input:
		u+=1
		for v in _:
			g.add_edge(u,v)
	# g.print_graph()
	g.dfs(1)