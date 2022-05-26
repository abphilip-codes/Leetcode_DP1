# 300
# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if(l<=1): return s
        a, b, z = 0, 1, 0
        while(z<l):
            if(l-z<=b/2): break
            y, k = z, z
            while(k<l-1 and s[k]==s[k+1]): k += 1
            z = k + 1
            while(k<l-1 and y and s[k+1]==s[y-1]):  k, y = k + 1, y - 1
            if(k-y+1>b): a, b = y, k - y + 1
        return s[a:a+b]