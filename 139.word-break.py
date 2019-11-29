#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        https://www.cnblogs.com/grandyang/p/4257740.html
        """
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for j in range(i,len(s)):  # 可以从dp的角度想以len(s)作为结束点
                    if s[i:j+1] in wordDict:
                        dp[j+1] = True
        return dp[-1]


        