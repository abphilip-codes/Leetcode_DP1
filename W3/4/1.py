# 300
# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        k = [nums[0]]
        for z in range(1,len(nums)):
            if(nums[z] > k[-1]): k.append(nums[z])
            else: k[bisect_left(k, nums[z], 0, len(k))] = nums[z]
        return len(k)