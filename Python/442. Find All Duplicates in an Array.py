class Solution(object):
    def findDuplicates(self, nums):
        nums.sort()
        a=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                a.append(nums[i])
        return a
    