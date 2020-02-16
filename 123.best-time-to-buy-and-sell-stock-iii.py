#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        我们定义local[i][j]为在到达第i天时最多可进行j次交易
        并且最后一次交易在最后一天卖出的最大利润，此为局部最优。
        然后我们定义global[i][j]为在到达第i天时最多可进行j次
        交易的最大利润，此为全局最优。
        """
        # if len(prices)==0:
        #     return 0
        # g = [0,0,0]
        # l = [0,0,0]
        # for i in range(len(prices)-1):
        #     diff = prices[i+1]-prices[i]
        #     for j in [2, 1]:
        #         l[j] = max(g[j-1]+max(diff,0), l[j]+diff)
        #         g[j] = max(l[j], g[j])
        # return g[2]

        """
        将整个操作过程当成4个人在操作，即一个做第一次买，
        一人做第一次卖，一人做第二次买，一人做第二次卖。
        买方的操作收益就是-price。第二次买卖需要依赖于
        第一次买卖的结果，这样可以保证两次买卖的一前一后顺序。
        """
        buy1 = float('-inf')
        buy2 = float('-inf')
        sell1 = 0
        sell2 = 0
        for item in prices:
            buy1 = max(buy1, -item)
            sell1 = max(sell1, buy1 + item)
            buy2 = max(buy2, sell1 - item)
            sell2 = max(sell2, buy2 + item)
        return sell2

    """
    https://www.cnblogs.com/grandyang/p/4281975.html
    https://www.jianshu.com/p/82b8949a3687
    """
        

