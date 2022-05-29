# 343
# https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        if(n==2): return 1
        if(n==3): return 2
        if(n%3==0): return int(pow(3, n//3))
        if(n%3==1): return int(pow(3, n//3-1)*4)
        if(n%3==2): return int(pow(3, n//3)*2)