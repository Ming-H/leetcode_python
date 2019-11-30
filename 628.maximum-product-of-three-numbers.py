#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        min1 = float('inf')
        min2 = float('inf')
        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')

        for item in nums:
            if item <= min1:
                min2 = min1
                min1 = item
            elif item <= min2:
                min2 = item
            if item >= max1:
                max3 = max2
                max2 = max1
                max1 = item
            elif item > max2:
                max3 = max2
                max2 = item
            elif item > max3:
                max3 = item
        return max(min1*min2*max1, max1*max2*max3)
# @lc code=end

