#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
            return [node(root, left, right)
                for root in range(first, last+1)
                for left in self.generateTrees(root-1, first)
                for right in self.generateTrees(last, root+1)] or [None]
    def node(self, val, left, right):
        node = TreeNode(val)
        node.left = left
        node.right = right
        return node
            



        