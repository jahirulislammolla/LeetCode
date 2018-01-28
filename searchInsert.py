class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=len(nums)
        x=[i for i in range(l) if nums[i]>=target]
        if x==[]:
            return l
        return x[0]
