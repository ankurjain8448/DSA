def partition(a, start, end):
	pivot = a[start]
	i = start + 1
	j = end
	while i < j :
		while i < j and a[i] < pivot :
			i += 1
		while i < j and a[j] > pivot:
			j -= 1
		a[i], a[j] = a[j], a[i]
	if pivot > a[i]:
		a[i], a[start] = a[start], a[i]
	else:
		i -= 1
		a[i], a[start] = a[start], a[i]
	return i

def quickSort(a, start, end):
	if start >= end :
		return
	index = partition(a, start, end)
	quickSort(a, start, index )
	quickSort(a, index + 1,end)


if __name__ == '__main__':
	a = [1,-4,2,9,5,8,6,0]
	n = len(a) -1
	quickSort(a,0,n)
	print a