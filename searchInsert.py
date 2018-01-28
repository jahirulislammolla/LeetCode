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
  #second way.............
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # l=len(nums)
        # x=[i for i in range(l) if nums[i]>=target]
        # if x==[]:
        #     return l
        # return x[0]
        x=len(nums)
        s,e=0,x
        #print(x)
        while s<e:
            x=(s+e)//2
            if  nums[x]<target:
                s=x+1
            if nums[x]>target:
                e=x
            if nums[x]==target:
                return x
        return s
