class CoinChangeOptimized(object):

	def set_some(self):
		self.temp = [0 for i in xrange(self.n+1)]
		self.matrix = [ [ 0 for i in xrange(len(self.c))] for i in xrange(self.n+1) ]

	def __init__(self, coins, n):
		self.n = n
		self.c = [ i for i in coins if i <= n]
		self.set_some()
		
	def cc_dp(self, coins, n):
		m = len(coins)
		table = [ [0 for i in xrange(len(coins))] for i in xrange(n+1)]
		for i in xrange(m):
			table[0][i] = 1 # set initial coins to 1
		for i in xrange(1, n+1):
			for j in xrange(m):
				val = 0
				coin = coins[j]
				# include coin
				if i-coin >=0:
					val += table[i-coin][j]
				# exclude coin
				if j>=1 :
					val += table[i][j-1]
				table[i][j] = val
		print table[n][m-1]
		return table[n][m-1]


	def pretty_print(self, a):
		print ">>>>>>"
		for i in a:
			print i

	def another_start_coinchange(self):
		'''
			This counts all the possible permutations
		'''
		self.set_some()
		n = self.n
		coins = self.c
		matrix = self.matrix
		temp = self.temp
		for i in xrange(1, n+1):
			for j in xrange(len(coins)):
				if i == coins[j]:
					matrix[i][j] = 1
				elif i > coins[j]:
					if i-coins[j] == i - 1 :
						matrix[i][j] = temp[i-coins[j]]
			# self.pretty_print(matrix)
			temp[i] = sum(matrix[i])
		print temp
		print temp[-1]


	def start_coinchange(self):
		'''
			This counts all the possible permutations
		'''
		self.set_some()
		n = self.n
		coins = self.c
		matrix = self.matrix
		temp = self.temp
		for i in xrange(1, n+1):
			for j in xrange(len(coins)):
				if i == coins[j]:
					matrix[i][j] = 1
				elif i > coins[j]:
					matrix[i][j] = temp[i-coins[j]]
			temp[i] = sum(matrix[i])
		print temp[-1]



class CoinChange(object):
	def __init__(self, coins, n):
		self.n = n
		self.c = [ i for i in coins if i <= n]

		self.path = []
		self.s = set()
		self.temp_count = [0]

	def cc(self, coins, m, n):
		if n ==0 :
			return 1
		if n < 0:
			return 0
		if m<= 0 and n >=1:
			return 0
		return self.cc(coins, m-1, n) + self.cc(coins, m, n - coins[m-1])
		
	def coin_change(self, n):
		if n == 0:
			self.temp_count[0]+=1
			temp = "".join(sorted([str(i) for i in self.path]))
			if temp not in self.s:
				self.s.add(temp)
		else:
			for i in self.c:
				if n-i>=0 :
					self.path.append(i)
					self.coin_change(n-i)
					self.path.pop()
	
	def start_coinchange(self):
		for i in self.c :
			if self.n-i>=0:
				self.path.append(i)
				self.coin_change(n-i)
				self.path.pop()
		print len(self.s)
		print self.temp_count

if __name__ == '__main__':
	coins = [3,1,2]
	# coins = map(int, raw_input().strip().split())
	n = 4

	obj = CoinChange(coins, n)
	print obj.cc(coins, len(coins), n)
	obj.start_coinchange()
	obj = CoinChangeOptimized(coins, n)
	obj.another_start_coinchange()
	obj.start_coinchange()
	print obj.cc_dp(coins, n)