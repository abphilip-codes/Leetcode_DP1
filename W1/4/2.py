# 45
# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        ans, m, k = 0, 0, 0
        for z in range(len(nums)-1):
            m = max(m, z+nums[z])
            if(k==z): ans, k = ans+1, m
        return ans