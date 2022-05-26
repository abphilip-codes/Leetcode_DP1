# 376
# https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if(s==s[::-1]): return len(s)
        n = len(s)
        arr = [0 for y in range(n)]
        arr[n-1] = 1

        for z in range(n-1, -1, -1):
            t = arr[:]
            t[z] = 1
            for y in range(z+1, n):
                if(s[z]==s[y]): t[y] = 2 + arr[y-1]
                else: t[y] = max(arr[y], t[y-1])
            arr = t
        return arr[n-1]