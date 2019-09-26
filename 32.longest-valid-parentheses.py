#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Time complexity : O(n). 
        Space complexity : O(1).
        """
        left = 0
        right = 0
        maxlength = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2*right)
            elif right > left:
                left = 0
                right = 0
        
        left = 0
        right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2*left)
            elif left>right:
                left = 0
                right = 0           
        return maxlength

