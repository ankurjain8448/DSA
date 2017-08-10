class SegmentTree(object):
	def __init__(self, arr):
		self.arr = arr
		self.N = 2*len(arr) -1
		self.ST = [0]*self.N
		self.create(0, 0, len(arr) - 1)

	def left(self, i):
		return 2*i +1

	def right(self, i):
		return 2*i + 2

	def create(self, sci, aci, ace):
		l = self.left(sci)
		r = self.right(sci)
		mid = (ace+ aci)/2
		if l < self.N:
			self.ST[sci] = max(self.create(l, aci, mid), self.create(r, mid+1, ace))
		else:
			self.ST[sci] = self.arr[aci]
		return self.ST[sci]

if __name__ == '__main__':
	arr = [2,3,4,6,1,9]
	print arr
	st = SegmentTree(arr)
	print st.ST