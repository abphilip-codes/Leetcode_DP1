# 516
# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        a, b, k = len(matrix), len(matrix[0]), 0
        arr = [[0 for _ in range(b+1)] for _ in range(a+1)]

        for z in range(1, a+1):
            for y in range(1, b+1):
                if(matrix[z-1][y-1]=="1"):
                    arr[z][y] = 1 + min(arr[z-1][y], arr[z][y-1], arr[z-1][y-1])
                    k = max(k, arr[z][y])
        return k*k