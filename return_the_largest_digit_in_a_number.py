class Solution:
    def largestDigit(self, n):
        maxi = 0
        if (n==0):
            return 0
        else:
            while(n!=0):
                ld = n%10
                if maxi < ld:
                    maxi =ld  
                else:
                    n=n//10
            
        return maxi