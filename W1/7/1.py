# 1014
# https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [values[0] + values[1]-1, max(values[1], values[0]-1)]
        for z in range(2, len(values)):
            dp[0] = max(dp[0], values[z] + dp[1]-1)
            dp[1] = max(dp[1]-1, values[z])
        return dp[0]