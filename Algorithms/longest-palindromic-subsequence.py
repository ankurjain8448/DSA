def lps(s, start, end):
	if start == end:
		return 1
	if s[start] == s[end] and start + 1 == end:
		return 2
	if s[start] == s[end]:
		return lps(s,start+1, end-1) + 2
	return max(lps(s, start, end-1), lps(s, start+1, end) )

def lps_iterative(string):
	n = len(string)
	matrix = [[0 for i in xrange(n)] for j in xrange(n)]

	for i in xrange(n):
		matrix[i][i] = 1

	for substring_length in xrange(2, n+1):
		for start_index in xrange(n - substring_length +1):
			end_index = start_index + substring_length - 1
			if string[start_index] == string[end_index] and substring_length == 2:
				matrix[start_index][end_index] = 2
			elif string[start_index] == string[end_index]:
				matrix[start_index][end_index] = matrix[start_index+1][end_index-1] + 2
			else:
				matrix[start_index][end_index] = max(matrix[start_index+1][end_index], matrix[start_index][end_index-1])
	for i in matrix:
		print i
	return matrix[0][n-1]

string = "ancdnn"
print lps(string, 0, len(string) - 1)
print lps_iterative(string)
