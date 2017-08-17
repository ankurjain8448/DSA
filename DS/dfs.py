from graph import Graph

class Graph(Graph):

	def dfs_allNodes(self):
		print "dfs_allNodes"
		self.visited = [False]*self.nodes
		for each_node in xrange(1, self.nodes):
			if not self.visited[each_node]:
				self.dfs_iterative(each_node)

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
				if not self.visited[each_node]:
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


if __name__ == '__main__':
	Input = [[2,4], [1,],[1,2,8,9],[1,3,5],[6,7],[],[],[10],[],[11],[]]
	nodes = len(Input)

	g = Graph(nodes)

	g.fill_graph(Input)
	# g.print_graph()
	g.dfs(1)
	# g.dfs_allNodes()