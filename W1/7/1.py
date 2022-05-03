# 1014
# https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        m, ans = values[-1]-len(values), 0
        for z in range(len(values)-2, -1, -1):
            m = max(m, values[z+1]-z-1)
            ans = max(ans, values[z]+z+m)
        return ans