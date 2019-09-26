#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, num, target):
        """
        Time complexity : O(n)
        Space complexity : O(n)
        """
        map = {}
        for i, item in enumerate(num):
            if item not in map:
                map[target-item] = i
            else:
                return map[item], i
        return -1,-1
