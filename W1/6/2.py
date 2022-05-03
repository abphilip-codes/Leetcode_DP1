# 1567
# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans, a, b, k = 0, -1, None, 1 
        for z in range(len(nums)):
            if(nums[z]==0): a, b, k = z, None, 1
            else:
                k *= nums[z] / abs(nums[z]) 
                if(k==1): ans = max(ans, z-a)
                else:
                    if b is None: b = z
                    ans = max(ans, z-b)
        return ans