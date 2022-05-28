# 518
# https://leetcode.com/problems/coin-change-2/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        arr = [0]*(amount+1)
        arr[0] = 1
        for z, k in enumerate(coins):
            for y in range(k, amount+1):
                arr[y] += arr[y-k]
        return arr[amount]