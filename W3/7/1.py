# 377
# https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        def f(nums, t, d, ans=0):
            if(t in d): return d[t]
            if(t==0): return 1
            if(t<0): return
            for z in nums:
                if(t>=z): ans+=f(nums, t-z, d)
                else: break
            d[t] = ans
            return ans
        return f(nums, target, {})