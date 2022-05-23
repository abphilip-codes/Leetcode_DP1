# 63
# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @lru_cache(None)
        def f(a=0, b=0):
            if(a>=m or b>=n or obstacleGrid[a][b]==1): return 0
            if(a==m-1 and b== n-1): return 1
            return f(a+1, b) + f(a, b+1)
        return f()