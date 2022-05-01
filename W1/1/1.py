# 509
# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if(n==0): return 0
        if(n==1): return 1
        a, b = 1, 1
        for i in range(1, n):
            b, a = a + b, b
        return a