#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(nums):
            now = prev = 0
            for n in nums:
                now, prev = max(now, prev + n), now
            return now
        return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))
        

