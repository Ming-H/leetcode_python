#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        https://www.cnblogs.com/slurm/p/5345985.html
        使用一个全局变量current_max，记录当前计算得出的最大路径。
        递归的思路：左子树中的最大路径和，右子树中的最大路径和，以
        及左子树中以root.left为起点的最大路径（需要大于零）+右子树
        中以root.right为起点的最大路径（需要大于零）+root.val），
        这三者中的最大值就是最大的路径和
        """
        def maxPathSum(root):  # DFS
            if root is None:
                return 0
            left = max(maxPathSum(root.left), 0)
            right = max(maxPathSum(root.right), 0)
            self.maxSum = max(self.maxSum, root.val + left + right)
            return max(left, right) + root.val
        self.maxSum = float('-inf')
        maxPathSum(root)
        return self.maxSum
        
        

    
       