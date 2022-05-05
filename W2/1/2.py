# 714
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        b, s = -prices[0], 0
        for z in range(1, len(prices)):
            b1, s1 = b, s
            b = max(b, s1 - prices[z])
            s = max(s, b1 + prices[z] - fee)
        return s