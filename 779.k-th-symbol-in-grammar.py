#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        """
        Time complexity: O(N)
        Space complexity: O(1)
        可以看作异或
        """
        ans = 0
        s, e = 1, 2**(N-1)
        while s<e:
            m = s+(e-s)//2
            if m < K:
                ans = ans^1 
                s = m+1
            else:
                e = m
        return ans
# @lc code=end

