#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]
        l = s + "#" +  rev_s
        p = [0] * len(l)
        for i in range(1,len(l)):
            j = p[i - 1]
            while j > 0 and l[i] != l[j]:
                j = p[j - 1]
            p[i] = j + (l[i] == l[j])
        return rev_s[:len(s) - p[-1]] + s

