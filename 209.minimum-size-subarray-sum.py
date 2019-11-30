#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        left = 0
        Sum = 0
        ans = float('inf')
        for i in range(len(nums)):
            Sum += nums[i]
            while Sum >= s:
                ans = min(ans, i+1-left)
                Sum -= nums[left]
                left += 1
        if ans!=float('inf'):
            return ans
        else:
            return 0  
    
   