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
		"""
			Print all nodes reachable from start_node, not all the nodes, i.e it 
			will not touch those nodes which are not connected to start_node via any path
		"""
		self.visited = [False]*self.nodes
		print "dfs_recursive"
		self.dfs_recursive(start_node)
		print "===="
		print "dfs_iterative"
		self.visited = [False]*self.nodes
		self.dfs_iterative(start_node)

	def dfs_recursive(self, start_node):
		"""
			Don't call me directly # call dfs
		"""
		if not self.visited[start_node]:
			self.visited[start_node] = True
			print "visited : ", start_node
			for each_node in self.graph[start_node]:
				self.dfs_recursive(each_node)

	def dfs_iterative(self, start_node):
		stack = [start_node]
		while stack:
			temp = stack.pop()
			if not self.visited[temp]:
				print "visited : ", temp
				self.visited[temp] = True
				for each_node in self.graph[temp]:
					if not self.visited[each_node]:
						stack.append(each_node)

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
	[1,3,5],
	[]
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