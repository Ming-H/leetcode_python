#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for item in matrix:
            if len(item) > 0 and item[-1] >= target:
                start, end = 0, len(item)-1
                while start <= end:
                    mid = (start + end) // 2
                    if item[mid] == target:
                        return True
                    elif item[mid] > target:
                        end = mid - 1
                    else:
                        start = mid + 1
                break
        return False
        
                


# @lc code=end

