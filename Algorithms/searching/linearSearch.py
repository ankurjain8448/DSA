def find(arr, n):
	for i in xrange(len(a)):
		if arr[i] == n:
			return True
	return False

if __name__ == '__main__':
	a = range(10)
	print find(a, 8)