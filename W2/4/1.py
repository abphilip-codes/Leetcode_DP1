# 264
# https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if(n<=6): return n
        a1, a2, a3 = 0, 0, 0 
        a = [1] + [0]*(n-1)
        for z in range(1, n):
            a[z] = min(a[a1]*2, a[a2]*3, a[a3]*5)
            if(a[z]==a[a1]*2): a1+=1
            if(a[z]==a[a2]*3): a2+=1
            if(a[z]==a[a3]*5): a3+=1
        return a[-1]