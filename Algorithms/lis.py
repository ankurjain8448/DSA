
def lis(a, i, n,index):
	# print "(i , a[i] : {}, {}), index : {} , a[index] : {}, n : {}".format(i, a[i], index, a[index], n )
	if i == n-1:
		return 0
	if a[i] >= a[index]:
		index = i
		return 1 + lis(a, i+1, n , index)
	return lis(a, i+1, n, index)

# b = [3, 4, 1, 2, 0, 3]
# b = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
b = [ 30, 92, 22, 48, 52, 64, 92, 50, 85, 38, 97, 15, 14, 75, 59, 46, 74, 6, 95, 67, 86, 88, 25, 49, 67, 69, 50, 99, 83, 49, 60, 6, 90, 1, 50, 41, 57, 18, 36, 5, 44, 100, 23, 33, 52, 11, 46, 49, 34, 27, 77, 57, 93, 82, 38, 95, 6, 51, 100, 32, 11, 26, 50, 3, 55, 39, 84, 54, 44, 75, 76, 51, 21, 40, 28, 50, 30, 6, 84, 58, 76, 42, 35, 49, 98, 49, 13, 101, 3, 1, 60, 48, 99, 70 ]
print b
def lis_iterative(arr):
	# returns the length of lis
	# print "111"
	n = len(arr)
	lis = [1]*n 
	for i in xrange (1, n):
		for j in xrange(i):
			if arr[i] >= arr[j] and lis[i]< lis[j] + 1 :
				lis[i] = lis[j]+1
	# print arr
	# print lis
	lis_length = max(lis)

	print lis[n-1]
	lis_arr = []
	temp = lis_length
	index = len(arr) -1
	while temp:
		if lis[index] == temp:
			lis_arr.append(arr[index])
			temp -= 1
		index -=1
	
	return lis_arr[::-1]
print lis_iterative(b)
