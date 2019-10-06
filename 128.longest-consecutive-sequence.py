#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(n)
        """
        length =0
        num_set = set(nums)
        for item in num_set:
            if item-1 not in num_set:
                current_num = item
                current_len = 1
                while current_num+1 in num_set:
                    current_num += 1
                    current_len += 1
                length = max(length, current_len)
        return length



# @lc code=end

