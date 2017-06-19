def print_lis(a):
	return "".join(a)
def swap(a, i, j):
	a[j],a[i] = a[i],a[j] 


def permute(a, i, j):
	if i == j :
		print print_lis(a)
	if i < j:
		for temp in xrange(i, j+1):
			swap(a, i, temp)
			permute(a, i+1 , j)
			swap(a, i, temp)


if __name__ == '__main__':
	a = ['a','b','c']
	n = len(a)-1
	permute(a, 0, n)
	print a