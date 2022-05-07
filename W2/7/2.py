# 304
# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = [list(accumulate(z))+[0] for z in matrix]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return sum(self.m[z][col2] - self.m[z][col1-1] for z in range(row1, row2+1))   


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)