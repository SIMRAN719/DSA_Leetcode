class Solution(object):
    def findDisappearedNumbers(self, nums):
        a=list(range(1,len(nums)+1))
        a=set(a)-set(nums)
        return list(a)