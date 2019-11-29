#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 
        locMin = locMax = gloMax = nums[0]
        for i in range(1, len(nums)):
            tmp = locMin
            locMin = min(locMin*nums[i], nums[i], locMax*nums[i]) 
            locMax = max(tmp*nums[i], nums[i], locMax*nums[i])
            gloMax = max(gloMax, locMax)
        return gloMax     



