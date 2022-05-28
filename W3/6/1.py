# 322
# https://leetcode.com/problems/coin-change/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = -1
        for z in range(len(s)):
            k = t.find(s[z], k+1)
            if(k==-1): return False
        return True