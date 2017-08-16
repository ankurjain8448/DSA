class SegmentTree(object):

	def get_correct_tree_size(self, arr_len):
		n = arr_len
		if n&(n-1) == 0: # check if n is 2**n form or not
			return 2*n -1
		else:
			count = 2
			while n > count:
				count *= 2
			return 2*count -1

	def __init__(self, arr):
		self.arr = arr
		self.N = self.get_correct_tree_size(len(arr))
		self.ST = [0]*self.N
		self.create(0, 0, len(arr) - 1)

	def left(self, i):
		return 2*i +1

	def right(self, i):
		return 2*i + 2

	def create(self, sci, aci, ace):
		l = self.left(sci)
		r = self.right(sci)
		if ace == aci:
			self.ST[sci] = self.arr[aci]
		else:
			mid = (ace + aci)/2
			self.ST[sci] = max(self.create(l, aci, mid), self.create(r, mid+1, ace))
		return self.ST[sci]

if __name__ == '__main__':
	arr = [2,3,4,6,9]
	print arr
	st = SegmentTree(arr)
	print st.ST