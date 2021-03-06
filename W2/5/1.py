# 118
# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = [1]*numRows
        for z in range(numRows): 
            a[z] = [1]*(z+1)
        for z in range(2, len(a)):
            for y in range(1, len(a[z])-1):
                a[z][y] = a[z-1][y-1]+a[z-1][y]
        return a