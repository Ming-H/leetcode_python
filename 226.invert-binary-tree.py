#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # if root:
        #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root

        # if not root:
        #     return None
        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)
        # root.left, root.right = right, left
        # return root

        if not root:
            return None
        queue = [root]
        while queue:
            current = queue.pop(0)
            tmp = current.left
            current.left = current.right
            current.right = tmp
            if current.left :
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root


        # if (root == null) return null;
        #     Queue<TreeNode> queue = new LinkedList<TreeNode>();
        #     queue.add(root);
        #     while (!queue.isEmpty()) {
        #         TreeNode current = queue.poll();
        #         TreeNode temp = current.left;
        #         current.left = current.right;
        #         current.right = temp;
        #         if (current.left != null) queue.add(current.left);
        #         if (current.right != null) queue.add(current.right);
        #     }
        #     return root;

            




