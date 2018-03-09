# -*- coding:utf-8 -*-
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    L = []
    for i in range(0, len(nums)-1):
        print('*******************','\n',nums[i])
        for j in (i+1, len(nums)-1):
            print(nums[j])
            # if (nums[i] + nums[j]) == target:
                # print(i,j)
                # if i not in L:
                    # L.append(i)
                # if j not in L:
                    # L.append(j)
    return L
    
if __name__ == "__main__":
    nums = [-3,4,3,90]
    target = 0
    print(twoSum(nums, target))
            
