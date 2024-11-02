class Solution:

    def checkprime(self, n):
        ct = 0
        for i in range(1,n+1):
            if(n%i==0):
                ct+=1
        
        if ct==2:
            return True
        else:
            return False

    def primeUptoN(self, n):

        count = 0
        for i in range(1,n+1):
            if self.checkprime(i) == True:
                count+=1
            
        return count