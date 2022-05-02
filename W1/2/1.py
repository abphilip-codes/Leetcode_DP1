# 70
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        l, r = 0, 1
        for z in range(n+1):
            k = l
            l = l + r
            r = k
        return l