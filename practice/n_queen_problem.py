def pretty_print(p):
	for i in p:
		print i

def can_place_at_index(matrix, i, j, n):
	temp_j = j
	temp_i = i

	while temp_i >=0:
		if matrix[temp_i][j] :
			return False
		temp_i -= 1
	temp_i = i -1 
	temp_j -= 1
	while temp_i >= 0 and temp_j >=0:
		if matrix[temp_i][temp_j]:
			return False
		temp_j -= 1
		temp_i -= 1

	temp_j = j + 1
	temp_i = i - 1
	while temp_i >= 0 and temp_j < n:
		if matrix[temp_i][temp_j]:
			return False
		temp_j+=1
		temp_i -=1
	return True


def start(matrix, row, n):
	if row>= n:
		# pretty_print(matrix)
		return True
	for i in xrange(n):
		can_place_at_i = can_place_at_index(matrix, row, i, n)
		if can_place_at_i:
			matrix[row][i] = 1
			if not start(matrix, row+1, n):
				matrix[row][i] = 0
			else:
				return True
	return False

def n_queen(n):
	board_size = [[0 for i in xrange(n)] for i in xrange(n)]
	start(board_size, 0, n)
	return board_size

n = 4
pretty_print(n_queen(n))