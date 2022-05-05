# 42
# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        ans, n = 0, len(height)
        a = b = 0
        if(n<=1): return 0
        while(True):
            while(b<n and height[b]<=height[a]): b+=1
            if(b==n): break
            ans+=(height[a]*(b-a-1)-sum(height[a+1:b]))
            a = b
        a, b = n-1, n-2
        while(True):
            while(b>=0 and height[b]<height[a]): b-=1
            if(b==-1): break
            ans+=(height[a]*(a-b-1)-sum(height[b+1:a]))
            a, b = b, b-1
        return ans