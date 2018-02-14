class Solution:
    def triangleNumber(self, nums):
        nums=sorted(nums)
        l=len(nums)
        count=0
        for i in range(l-2):
            k=i+2
            for j in range(i+1,l-1):
                s=nums[i]+nums[j]
                if k==j:
                    k+=1
                while(k<l):
                    if s<=nums[k]:
                        break
                    k+=1
                count+=k-j-1
        return count
