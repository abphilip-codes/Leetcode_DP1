# 1567
# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        for arr in [nums, nums[::-1]]:
            a, b, k = 0, 0, 0
            for z in arr:            
                if(z==0): a, b = 0, 0
                elif(z<0): a+=1
                elif(z>0): b+=1
                k = max((a+b) if(a%2==0) else 0, k)
            ans = max(k, ans)
        return ans