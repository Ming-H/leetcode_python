#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, n, k, path, res):
            if k==0:
                res.append(path)
                return
            for i in range(i+1, n+1):
                dfs(i, n, k-1, path+[i], res)  
        dfs(0, n, k, [], res)
        return res



# @lc code=end

