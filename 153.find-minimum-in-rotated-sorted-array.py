#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
<<<<<<< HEAD

# @lc code=start
=======
>>>>>>> f1c90e3e142a52529829175e0dda84b11678cc13
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid]>nums[right]:
                left = mid + 1
            else:
                right = mid 
        return nums[left]
<<<<<<< HEAD
# @lc code=end
=======
        
>>>>>>> f1c90e3e142a52529829175e0dda84b11678cc13

