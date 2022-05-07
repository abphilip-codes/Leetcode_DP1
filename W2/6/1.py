# 931
# https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), 10001
        for z in range(n-2, -1, -1):
            for y in range(n):
                a1 = matrix[z+1][y-1] if(y>0) else m 
                a2 = matrix[z+1][y+1] if(y<n-1) else m
                matrix[z][y] = matrix[z][y] + min(a1, matrix[z+1][y], a2)
        return min(matrix[0])