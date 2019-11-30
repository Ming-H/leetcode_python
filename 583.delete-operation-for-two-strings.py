#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        lcs = [[0] * (l1+1) for _ in range(l2+1)]
        # print(lcs)
        for i in range(1, l2+1):
            for j in range(1, l1+1):
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], lcs[i-1][j-1]+(word2[i-1]==word1[j-1]))
        return l1 + l2 - 2 * lcs[l2][l1]
# @lc code=end

