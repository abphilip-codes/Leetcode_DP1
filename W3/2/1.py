# 64
# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        a, b = len(grid), len(grid[0])
        arr = [[0]*(b) for z in range(a)]
        
        for z in range(a):
            for y in range(b):
                k = min(arr[z-1][y] if(z>0) else float('inf'), \
                        arr[z][y-1] if(y>0) else float('inf'))
                
                arr[z][y] = grid[z][y] + (k if k!=float('inf') else 0)
        return arr[-1][-1]