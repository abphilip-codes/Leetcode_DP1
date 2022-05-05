# 309
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0 
        n = len(prices)
        b, s = [0]*n, [0]*n
        b[0] = -prices[0]

        for z in range(1, n):
            s[z] = max(s[z-1], b[z-1] + prices[z])
            b[z] = max(b[z-1], s[z-2] - prices[z])
        return max(s[-1], s[-3]) if(len(s)>2) else s[-1]