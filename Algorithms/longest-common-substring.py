def longestCommonSubstring(a, b):
	'''
	Time Complexity : O(n*m)
	Space Complexity : O(n*m)

	Space Complexity can be optimized to : O(min(m, n))
	'''
	n = len(a)
	m = len(b)
	max_length = 0
	matrix = [[0 for i in xrange(n)] for j in xrange(m)]
	for i in xrange(n):
		if b[0] == a[i]:
			matrix[0][i] = 1
			max_length = 1

	for i in xrange(m):
		if b[i] == a[0]:
			matrix[i][0] = 1
			max_length = 1

	for i in xrange(1, m):
		for j in xrange(1, n):
			if b[i] == a[j]:
				matrix[i][j] = matrix[i-1][j-1] + 1
				max_length = max(max_length, matrix[i][j])
			else:
				matrix[i][j] = 0
	
	for i in matrix:
		print i
	
	for i in xrange(max_length-1, m):
		for j in xrange(max_length-1, n):
			if matrix[i][j] == max_length:
				print b[i- max_length +1 :i +1]
				break
	print max_length

a = "OldSited"
b = "NewSitex"
longestCommonSubstring(a, b)