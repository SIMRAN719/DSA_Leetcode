class Solution(object):
    def intersection(self, nums1, nums2):
        nums3=[]
        if len(nums1)<len(nums2):
            length=len(nums1)
            x,y=nums1,nums2
        else:
            length=len(nums2)
            x,y=nums2,nums1
        for i in range(length):
            if ((x[i] in y) and (x[i] not in nums3)):
                nums3.append(x[i])
        return nums3