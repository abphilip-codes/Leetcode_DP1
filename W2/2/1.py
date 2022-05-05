# 139
# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        a = [True] + [False]*n
        for z in range(n):
            for y in range(z+1, n+1):
                if(a[z] and not a[y] and s[z:y] in wordDict): a[y] = True
        return a[-1]