class Solution(object):
    def hammingWeight(self, n):
        count=0
        while n!=0:
            a=n%10
            if a==1:
                count+=1
            n=n//10
        return count