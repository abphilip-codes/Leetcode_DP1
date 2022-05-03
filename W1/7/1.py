# 1014
# https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def rob(self, nums: List[int]) -> int:
        a, s = 0, 0
        for z in nums: a, s = z+s, max(a, s)
        return max(a, s)