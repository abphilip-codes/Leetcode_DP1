# 96
# https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:        
        d = {}
        for z in range(n+1):
            if(z<=1): d[z] = 1
            else: d[z] = sum(d[y]*d[z-y-1] for y in range(z))
        return d[n]