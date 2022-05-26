# 376
# https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        ans, k = 1, None
        for z in range(len(nums)-1):
            if(nums[z+1]-nums[z]==0): continue
            if(nums[z+1]-nums[z]>0):
                if(k==None or k==False): ans+=1
                k = True
            if(nums[z+1]-nums[z]<0):
                if(k==None or k==True): ans+=1
                k = False
        return ans