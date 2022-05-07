# 120
# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for z in range(len(triangle)-2, -1, -1):
            for y in range(len(triangle[z])):
                triangle[z][y] += min(triangle[z+1][y], triangle[z+1][y+1])
        return triangle[0][0]