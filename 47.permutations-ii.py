#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length == 0: 
            return []
        if length == 1: 
            return [nums]
        nums.sort()
        res = []
        previousNum = None
        for i in range(length):
            if nums[i] == previousNum: 
                continue
            previousNum = nums[i]
            for j in self.permuteUnique(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)
        return res

