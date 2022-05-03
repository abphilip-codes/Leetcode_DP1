# 55
# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        a, b = n-2, n-1
        while(a>=0):
            if(nums[a]+a>=b): b=a
            a-=1
        return (b==0)