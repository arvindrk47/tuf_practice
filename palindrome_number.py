class Solution:
    def isPalindrome(self, n):
        pa = 0
        dup= n 
        if n==0:
            return (dup==n)
        else:
            while(n!=0):
                last = n%10
                n=n//10
                pa = (pa*10)+ last
            return (dup==pa)