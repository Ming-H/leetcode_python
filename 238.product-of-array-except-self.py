#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:   
        """
        Time complexity : O(N)
        Space complexity : O(1)
        """
        length = len(nums)
        answer = [1]*length
        # answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        
        R = 1
        for i in reversed(range(length)):
            answer[i] *= R
            R *= nums[i]
        
        return answer
        
        # res = []
        # from functools import reduce
        # product = reduce(lambda x,y: x * y, nums)
        # for item in nums:
        #     res.append(int(product/item))
        # return res


