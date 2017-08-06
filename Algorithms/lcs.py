def lcs(a, b, i, j):
	if i == 0 or j == 0:
		return 0
	if a[i-1] == b[j-1]:
		return 1 + lcs(a,b,i-1,j-1)
	return max(lcs(a,b,i-1,j), lcs(a,b,i,j-1))

def lcs_iterative(a, b):
	n = len(a)
	m = len(b)
	matrix = [[0 for i in xrange(n)] for j in xrange(m)]

	for i in xrange(n):
		if b[0] == a[i]:
			matrix[0][i] = 1

	for i in xrange(m):
		if b[i] == a[0]:
			matrix[i][0] = 1

	for i in xrange(1, m):
		for j in xrange(1, n):
			if b[i] == a[j]:
				matrix[i][j] = matrix[i-1][j-1] + 1
			else:
				matrix[i][j] = max(matrix[i][j-1],matrix[i-1][j])
	
	# print lcs
	arr = []
	lcs_length = matrix[m-1][n-1]
	r = m-1
	c = n-1
	for i in matrix:
		print i
	while r > -1 and c > -1:
		if r>-1 and c>-1 and  a[c] == b[r]:
			arr.append(a[c])
			r -= 1 ; c -= 1
		else:
			if r > 0 and c > 0 and matrix[r-1][c] > matrix[r][c-1]:
				r -= 1
			else:
				c -= 1

	print arr[::-1]

a = [1, 2, 3, 4, 1]
b = [3, 4, 1, 2, 1, 3]
a = 'abcdee'
b = 'cdbefe'
# a = 'abcdxyzo'
# b = 'axozbmdllo'
# print lcs(a,b, len(a), len(b))
# lcs_iterative(a,b)