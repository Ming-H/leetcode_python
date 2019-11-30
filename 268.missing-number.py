#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # missing = len(nums)
        # for i, num in enumerate(nums):
        #     missing ^= i ^ num
        # return missing
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


