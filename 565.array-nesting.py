#
# @lc app=leetcode id=565 lang=python3
#
# [565] Array Nesting
#

# @lc code=start
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        res = 0
        for i in range(len(nums)):
            if nums[i] != float('inf'):
                start = nums[i]
                count = 0
                while nums[start]!=float('inf'):
                    tmp = start
                    start = nums[start]
                    count += 1
                    nums[tmp] = float('inf')
                res = max(res, count)

        return res
# @lc code=end

