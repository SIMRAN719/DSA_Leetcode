class Solution(object):
    def singleNumber(self, nums):
        a=[]
        for i in nums:
            if i in a:
                a.remove(i)
            else:
                a.append(i)
        return a[0]