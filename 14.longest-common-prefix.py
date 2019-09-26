#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        str0=strs[0]
        Min=len(str0)
        for i in range(1,len(strs)):
            j=0
            p=strs[i]
            while j<Min and j<len(p) and p[j]==str0[j]:
                j+=1
            Min = min(Min, j)
        return str0[:Min]

