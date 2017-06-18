from graph import Graph

class Graph(Graph):
	
	def bfs(self, start_node):
		queue = [start_node]
		while queue:				
			temp = queue.pop(0)
			if not self.visited[temp]:
				print temp
				self.visited[temp] = True
				for each in self.graph[temp]:
					if not self.visited[each]:
						queue.append(each)



if __name__ == '__main__':
	Input = [
				[2,4],
				[1,],
				[1,2,8,9],
				[1,3,5],
				[6,7],
				[],
				[],
				[],
				[]
			]
	nodes = len(Input)

	g = Graph(nodes)

	g.fill_graph(Input)
	g.bfs(1)
