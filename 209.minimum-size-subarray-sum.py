#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        left = 0
        right = 0
        sum = 0
        res = len(nums)+1
        while right<len(nums):
            while sum<s and right<len(nums):
                sum += nums[right]
                right += 1
            while sum>=s:
                res = min(res, right-left)
                sum -= nums[left]
                left += 1
        if res == len(nums)+1:
            return 0
        else:
            return res


        
# @lc code=end

