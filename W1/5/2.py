# 918
# https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        l, ans, h, k = len(nums), nums[0], [(0,-1)], 0
        for z in range(2*l):
            k += nums[z%l]
            while(h and z-h[0][1]>l): heappop(h)            
            ans = max(ans,k-h[0][0])
            heappush(h,(k,z))
        return ans