class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            x=target-nums[i]
            if x in nums:
                for j in range(i+1,len(nums)):
                    if x==nums[j]:
                        return [i,j]
