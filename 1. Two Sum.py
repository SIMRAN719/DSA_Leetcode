class Solution(object):
    def twoSum(self, nums, target):
        a=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    a.append(i)
                    a.append(j)
        return a