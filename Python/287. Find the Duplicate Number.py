class Solution(object):
    def findDuplicate(self, nums):
        a=set()
        for i in nums:
            if i in a:
                return i
            a.add(i)
        return None