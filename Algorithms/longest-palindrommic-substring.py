class Solution(object):
	def get_length(self, string, i, strlen):
		start_index = i
		end_index = i

		while start_index - 1 >=0 and string[start_index-1] == string[i]:
			start_index -= 1

		while end_index + 1 < strlen and string[end_index + 1] == string[i]:
			end_index += 1

		diff = (end_index - start_index + 1)

		actual_start_index = start_index
		start_index -= 1
		end_index += 1

		while start_index >= 0 and end_index < strlen:
			if string[start_index] != string[end_index]:
				break
			else:
				diff += 2
				actual_start_index -= 1
			start_index -= 1
			end_index += 1
		return actual_start_index , diff


	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		n = len(s)
		if n < 2:
			return s
		max_length = 0
		start_index = 0
		for i in xrange(1, n):
			s_index , length = self.get_length(s, i, n)
			if length > max_length:
				max_length = length
				start_index = s_index
		return s[start_index: start_index + max_length]

s = "babad"
# s = "ccc"
# s = "  "
obj = Solution()
print obj.longestPalindrome(s)
