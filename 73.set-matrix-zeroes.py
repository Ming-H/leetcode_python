#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        1、行从0开始，如果第一列有元素是0，则列标签为True，列从1开始，如果元素
            是0，则行、列的头置为0
        2、行列均从1开始，如果行列开头为0，则该元素置为0
        3、如果第一个元素为0，则第一行为0
        4、如果列标签为True，第一列为0
        """
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            # if matrix[i][0] == 0:
            #     is_col = True
            for j in range(C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j] == 0:
                    if j==0:
                        is_col = True
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R): 
            for j in range(1, C):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if is_col:
            for i in range(R):
                matrix[i][0] = 0
        
# @lc code=end

