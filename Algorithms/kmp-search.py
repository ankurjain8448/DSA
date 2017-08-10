class KMP(object):
	def calculate_phi(self, pattern):
		'''
			phi : contains, length of longest suffix which is the proper prefix for P[0..i]
		'''
		n = len(pattern)
		phi = [0]*n
		for i in xrange(1, n):
			j = i
			while j > 0 and pattern[i] != pattern[phi[j-1]]:
				j = phi[j-1]
			if j == 0:
				if pattern[i] == pattern[j]:
					phi[i] = 1
			else:
				phi[i] = phi[j-1] + 1
		print phi
		return phi

	def search(self, text, pattern):
		phi = self.calculate_phi(pattern)
		p_len = len(pattern)
		j = 0 # j is patten_current_index
		i = 0 # i is text_current_index
		text_len = len(text)
		while  i < text_len:
			if text[i] == pattern[j]:
				i += 1
				j += 1
				if j == p_len:
					print "match occured at text {} ".format(i - p_len)
					break
			else:
				# shifting in pattern
				if j != 0:
					j = phi[j-1]
				else:
					i += 1
		else:
			print "no match"



obj = KMP()
# obj.search('asdabcabak', 'aba')
obj.search('abacacpiabacbkdcs', 'abacab')