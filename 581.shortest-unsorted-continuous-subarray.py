#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        if len(nums)<2:
            return 0
        
        Min = float('inf')
        Max = float('-inf')
            
        for i in range(1, len(nums)):
        	if nums[i] < nums[i-1]:
        		Min = min(Min, nums[i])
        
        for i in range(len(nums)-2, -1, -1):
        	if nums[i]>nums[i+1]:
        		Max = max(Max, nums[i])

        for l in range(len(nums)):
        	if Min < nums[l]:
        		break
        for r in range(len(nums)-1, -1, -1):
        	if Max > nums[r]:
        		break

        if r-l<0:
        	return 0
        else:
        	return r-l+1
# @lc code=end

