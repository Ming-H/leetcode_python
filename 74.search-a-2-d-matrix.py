#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if len(matrix[0]) != 0 and matrix[i][len(matrix[0])-1]\
                                             >= target:
                start = 0; end = len(matrix[0])-1
                while start <= end:
                    mid = (start + end) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        end = mid - 1
                    else:
                        start = mid + 1
                break
        return False


# @lc code=end

