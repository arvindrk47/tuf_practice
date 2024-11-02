class Solution:
    def isPrime(self, n):
        #your code goes here
        ct =0
        for i in range(1,n+1):
            if n%i==0:
                ct+=1
        if (ct==2):
            return True
        else:
            return False