# 121
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def rob(self, nums: List[int]) -> int:
        a1, b1, a2, b2 = nums[0], 0, 0, 0
        for z in nums[1:-1]:
            a1, b1 = z+b1, max(a1, b1)
            a2, b2 = z+b2, max(a2, b2)
        return max(a1, b1, nums[-1]+b2, a2)