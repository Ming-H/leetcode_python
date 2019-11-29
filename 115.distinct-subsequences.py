#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        dp method
        https://blog.csdn.net/XX_123_1_RJ/article/details/80789223
        """
        m, n = len(s)+1, len(t)+1
        dp = [0] * n  # 初始化dp
        dp[0] = 1
 
        for j in range(1, m):
            pre = dp[:]  # pre 表示前一列的值
            for i in range(1, n):
                dp[i] = pre[i] + pre[i - 1] * (t[i - 1] == s[j - 1])
        return dp[-1]
        
