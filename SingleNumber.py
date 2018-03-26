"""
给定一个整数数组，除了某个元素外其余元素均出现两次。请找出这个只出现一次的元素。
备注：
你的算法应该是一个线性时间复杂度。 你可以不用额外空间来实现它吗？
思路：
一个整数和它本身异或之后得到值是0，0与其他整数异或得到的是这个整数本身
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 2:
            return False
        elif len(nums) == 1:
            return nums
        else:
            num = 0
            for item in nums:
                num = num ^ item
            return num
        
