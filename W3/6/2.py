# 518
# https://leetcode.com/problems/coin-change-2/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1, k, ans = defaultdict(deque), [], []
        for y, z in enumerate(text1):
            if(z in set(text2)): t1[z].appendleft(y)
        for z in text2:
            if(z in set(text1)): k += list(t1[z])
        for z in k:
            y = bisect_left(ans, z)
            if(y==len(ans)): ans.append(z)
            else: ans[y] = z
        return len(ans)