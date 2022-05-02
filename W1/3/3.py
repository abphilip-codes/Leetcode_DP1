# 740
# https://leetcode.com/problems/delete-and-earn/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        l, r = 0, 0
        for z in range(max(c)+1):
            k = max(l + (c[z]*z), r)
            l, r = r, k
        return max(l, r)