class Solution:
    def countDigit(self, n):
        count = 0
        if n==0:
            return 1
        else:
            while(n!=0):
                n=n//10
                count+=1
            return count