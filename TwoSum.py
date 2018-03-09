# -*- coding:utf-8 -*-
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    print(i,j)
        return i,j


    
if __name__ == "__main__":
    nums = [-3,4,3,90]
    target = 0
    ss = Solution()
    ss.twoSum(nums, target)
            
