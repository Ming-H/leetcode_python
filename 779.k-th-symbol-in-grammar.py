#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        mapping = ((0, 1), (1, 0))
        if N == 1:
            return 0
        return mapping[self.kthGrammar(N - 1, K // 2 + K % 2)][(K - 1) % 2]
# @lc code=end

