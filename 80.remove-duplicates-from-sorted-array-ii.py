#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3: 
            return len(nums)
        i = 1
        for j in range(1, len(nums)-1):
            if nums[j-1] != nums[j+1]:
                nums[i] = nums[j]
                i += 1
        nums[i] = nums[-1]
        return i + 1

