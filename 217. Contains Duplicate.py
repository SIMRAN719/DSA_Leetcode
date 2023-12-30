class Solution(object):
    def containsDuplicate(self,nums):
        b=False
        a=set()
        for i in range(len(nums)):
            if nums[i] not in a:
                a.add(nums[i])
            else:
                b= True 
                break
        return b