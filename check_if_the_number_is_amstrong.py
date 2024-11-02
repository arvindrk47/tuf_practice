class Solution:
    def isArmstrong(self, n):
        p = len(str(n))
        dup = n
        result = 0
        a = str(n)
        for i in range(p):
            result = result + int(a[i])**p 

        return (result == dup) 
            

