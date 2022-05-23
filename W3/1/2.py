# 63
# https://leetcode.com/problems/unique-paths-ii/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        if(m==0 or n==0): return
        self.arr = [[0]*(n+1) for z in range(m+1)]
        for z in range(1,m+1):
            for y in range(1,n+1):
                self.arr[z][y] = self.arr[z][y-1] + self.arr[z-1][y] + matrix[z-1][y-1] - self.arr[z-1][y-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.arr[row2+1][col2+1] - self.arr[row1][col2+1] - self.arr[row2+1][col1] + self.arr[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)