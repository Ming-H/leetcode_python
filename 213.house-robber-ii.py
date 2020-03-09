#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        # def helper(nums):
        #     now = prev = 0
        #     for n in nums:
        #         now, prev = max(now, prev + n), now
        #     return now
        # return max(helper(nums[len(nums) != 1:]), helper(nums[:-1]))

        # https://blog.csdn.net/fuxuemingzhu/article/details/82982325

        if not nums: 
            return 0
        if len(nums) == 1: 
            return nums[0]
        if len(nums) == 2: 
            return max(nums[0], nums[1])
        return max(self.rob_range(nums[:len(nums)-1]), \
                        self.rob_range(nums[1:]))
    
    def rob_range(self, nums):
        if not nums: 
            return 0
        if len(nums) == 1: 
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

