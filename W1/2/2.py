# 746
# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = cost[-2]
        r = cost[-1]
        for z in range(len(cost)-3, -1, -1):
            k = cost[z] + min(l, r)
            l, r = k, l
        return min(l, r)