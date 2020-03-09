#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(n)
        https://www.cnblogs.com/grandyang/p/6529857.html
        """
        d = {0:-1}
        maxlen, count = 0, 0
        for i in range(len(nums)):
            count = count+1 if nums[i]==1 else count-1
            if count in d:
                maxlen = max(maxlen, i-d[count])
            else:
                d[count] = i
        return maxlen

        

# @lc code=end

