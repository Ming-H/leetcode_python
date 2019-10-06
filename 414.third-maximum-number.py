#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums=set(nums)
        len_set_nums=len(set_nums)
        max_num=max(nums)
        min_num=min(nums)
        if len_set_nums<3:
            return max_num
        if len_set_nums==3:
            return min_num
        else:
            first_max=max_num
            second_max=float('-inf')
            third_max=float('-inf')
            for num in set_nums:
                if num>second_max and num<first_max:
                    second_max,third_max=num,second_max
                elif num>third_max and num<second_max:
                    third_max=num
            return third_max     

        # nums = set(nums)
        # for _ in range((2, 0)[len(nums) < 3]): 
        #     nums.remove(max(nums))
        # return max(nums)
# @lc code=end

