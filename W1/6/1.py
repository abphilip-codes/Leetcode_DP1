# 152
# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx1, mn1 = 1, 1
        ans = nums[0]
        for z in nums:
            mx2, mn2 = mx1, mn1
            mx1 = max(z, mx2 * z, mn2 * z)
            mn1 = min(z, mx2 * z, mn2 * z)
            ans = max(ans, mx1)
        return ans