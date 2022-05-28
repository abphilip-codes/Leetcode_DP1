# 322
# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if(amount==0): return 0
        arr = [0]+[math.inf]*amount
        coins = sorted(coins)
        for z in range(1,amount+1):
            if(z>=coins[0]): 
                arr[z] = 1 + min(arr[z-y] for y in coins if(y<=z))
        return arr[-1] if(arr[-1]<=amount) else -1