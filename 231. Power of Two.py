class Solution(object):
    def isPowerOfTwo(self, n):
        x=1
        while x<=n:
            if x==n:
                return True
            x= x*2
        return False 