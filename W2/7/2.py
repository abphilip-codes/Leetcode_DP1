# 304
# https://leetcode.com/problems/range-sum-query-2d-immutable/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for z in range(rowIndex+1):
            k = (math.factorial(rowIndex) // 
                (math.factorial(z) * math.factorial(rowIndex-z)))
            ans.append(k)
        return ans