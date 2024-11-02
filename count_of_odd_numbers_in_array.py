class Solution:
	def countOdd(self, arr, n):
		ct = 0
		for i in range(n):
			if arr[i]%2 !=0:
				ct+=1
		return ct
