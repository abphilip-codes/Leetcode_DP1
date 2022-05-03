# 53
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for z in range(1, len(nums)):
            if(nums[z-1]>0): nums[z]+=nums[z-1]
        return max(nums)