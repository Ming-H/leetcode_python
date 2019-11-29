#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n==0:
            return 0
        
        dp = [0 for i in range(n)]
        tmp=0
        for i in range(1,3):
            balance = -prices[0]
            tmp = dp[0]
            for j in range(1, n):
                copy = dp[j]
                dp[j] = max(dp[j-1], balance+prices[j])
                balance = max(balance, tmp-prices[j])
                tmp = copy
        return dp[n-1]

    """
    https://blog.csdn.net/laputafallen/article/details/79846424
    """
        

