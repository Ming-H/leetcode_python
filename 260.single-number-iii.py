#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # https://leetcode.com/discuss/48119/single-number-iii
        xor = 0
        for num in nums: 
            xor ^= num
        xor = xor & (xor - 1) ^ xor
        a = b = 0
        for num in nums:
            if xor & num:
                a ^= num
            else:
                b ^= num
        return [a, b]
# @lc code=end

