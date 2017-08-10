'''
	A list contains numbers(integers), concatinate the integers to make the largest number possible
'''
def other_comp(a, b):
	# a>b in length
	b_curr_index = 0
	b_len = len(b)
	a_len = len(a)
	for i in xrange(b_len, a_len):
		p , q = int(a[i]), int(b[b_curr_index])
		if p > q:
			return 1
		elif p < q:
			return -1
		b_curr_index += 1
		if b_curr_index == b_len:
			b_curr_index = 0
	return 1

def compare(a, b):
	l1 = len(a)
	l2 = len(b)

	for i in xrange(min(l1, l2)):
		p , q = int(a[i]), int(b[i])
		if p > q:
			return 1
		elif p < q:
			return -1
	if l1 == l2:
		return 1
	if l1 > l2:
		return other_comp(a, b)
	else:
		val = other_comp(b, a)
		if val == 1:
			return -1
		else:
			return 1


def concat(lis):
	temp = map(str, lis)
	temp.sort(reverse=True)
	# temp.sort(compare, reverse = True)
	return "".join(temp)


a = [1,2,4,4,4,4,4444,5,55,789,12,79,1,11,111,112,1111112]
print concat(a)