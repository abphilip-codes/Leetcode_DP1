# 62
# https://leetcode.com/problems/unique-paths/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        a = [[0]*(n+1) for _ in range(m+1)]
        for z in range(1, m+1):
            for y in range(1, n+1):
                a[z][y] = a[z-1][y] + a[z][y-1] - a[z-1][y-1] + mat[z-1][y-1]

        def f(z1, y1, z2, y2):
            z1 = max(z1, 1)
            z2 = min(z2, m)
            y1 = max(y1, 1)
            y2 = min(y2, n)
            return a[z2][y2] - a[z1-1][y2] - a[z2][y1-1] + a[z1-1][y1-1]
        
        ans = [[0]*n for _ in range(m)]
        for z in range(1,m+1):
            for y in range(1,n+1):
                ans[z-1][y-1] = f(z-k,y-k,z+k,y+k)
        return ans