#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        minprice = float("inf")
        maxprofit = 0
        for item in prices:
            if item < minprice:
                minprice = item
            elif item - minprice > maxprofit:
                maxprofit = item - minprice
        return maxprofit


        
# @lc code=end

