class Solution:
    def largestElement(self, nums):
        l = 0
        for num in nums:
            if num > l:
                l = num
        return l
