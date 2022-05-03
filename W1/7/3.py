# 122
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = -prices[0], 0
        for z in range(1, len(prices)):
            b, s = max(b, s-prices[z]), max(s, b+prices[z])
        return s