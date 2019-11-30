#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for i, v in enumerate(nums):
            if v in dict and i-dict[v] <= k:
                return True
            dict[v] = i
        return False

