#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
class Solution:
    # DP 
    def numTrees(self, n: int) -> int:
        # https://www.cnblogs.com/grandyang/p/4299608.html
        # https://www.jianshu.com/p/c3dd041d3e21
        res = [0] * (n+1)
        res[0] = 1
        res[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]
    

