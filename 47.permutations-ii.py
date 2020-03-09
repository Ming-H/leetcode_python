#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(nums, pre, path, res):
            if len(nums) == 0:
                res.append(list(path))
            pre = None
            for i in range(len(nums)):
                if nums[i] == pre:
                    continue
                path.append(nums[i])
                dfs(nums[:i] + nums[i+1:], nums[i], path, res)
                path.pop()
                pre = nums[i]
        dfs(nums, None, [], res)
        return res

    
