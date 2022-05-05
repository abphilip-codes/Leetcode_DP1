# 264
# https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l = len(nums)
        if(l<3): return 0
        ans, k, n = 0, 1, nums[0]-nums[1]
        for z in range(2, l):
            p = nums[z-1]-nums[z]
            if(n==p): k+=1
            else:
                n = p
                if(k>1): ans, k = ans+((k+1)*(k-2)//2+1), 1    
        return ans+((k+1)*(k-2)//2+1)