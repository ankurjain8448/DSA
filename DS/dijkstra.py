import sys

class Graph(object):
	def __init__(self, inputs):
		self.nodes = len(inputs[0])
		self.graph = inputs
		self.max_value = sys.maxint

	def get_min_distance_node(self):
		min_distance = self.max_value
		node = None
		for i in xrange(self.nodes):
			if not self.visited[i] and min_distance >= self.distance_arr[i]:
				min_distance = self.distance_arr[i]
				node = i
		return node

	def dijkstra(self, node):
		self.visited = [False]*self.nodes
		self.distance_arr = [self.max_value]*self.nodes
		
		self.distance_arr[node] = 0
		for i in xrange(self.nodes):
			u = self.get_min_distance_node()
			self.visited[u] = True
			for v in xrange(self.nodes):
				if self.graph[u][v] > 0  and not self.visited[v] and self.distance_arr[v] > self.distance_arr[u] + self.graph[u][v]:
					self.distance_arr[v] = self.distance_arr[u] + self.graph[u][v]
		print self.distance_arr

if __name__ == '__main__':
	Input = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ]
	g = Graph(Input)
	source_node = 0
	g.dijkstra(source_node)