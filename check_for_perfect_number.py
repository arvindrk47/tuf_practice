class Solution:
    def isPerfect(self, n):
        result = 0
        dup = n
        for i in range(1,n):
            if n%i == 0:
                result+=i
        return (result==dup)