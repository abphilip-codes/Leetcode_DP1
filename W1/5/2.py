# 918
# https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n, s = len(nums), nums[0]
        c1, c2, g1, g2 = nums[0], nums[0], nums[0], nums[0]
        for z in range(1, n):
            c1 = min(nums[z], nums[z]+c1)
            g1 = min(g1, c1)
            c2 = max(nums[z], nums[z]+c2)
            g2 = max(g2, c2)
            s += nums[z]
        return g2 if(g2>(s-g1) or not (s-g1)) else (s-g1)