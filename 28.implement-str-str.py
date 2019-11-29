#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        KMP的整体时间复杂度为O(m + n)。
        https://blog.csdn.net/liuxiao214/article/details/78026473
        KMP字符串匹配的主函数
        若存在字串返回字串在字符串中开始的位置下标，或者返回-1
        '''
        pnext = self.gen_pnext(needle)
        n = len(haystack)
        m = len(needle)
        i, j = 0, 0
        while (i<n) and (j<m):
            if (haystack[i]==needle[j]):
                i += 1
                j += 1
            elif (j!=0):
                j = pnext[j-1]
            else:
                i += 1
        if (j == m):
            return i-j
        else:
            return -1
            
    def gen_pnext(self, substring):
        """
        构造临时数组pnext
        """
        index, m = 0, len(substring)
        pnext = [0]*m
        i = 1
        while i < m:
            if (substring[i] == substring[index]):
                pnext[i] = index + 1
                index += 1
                i += 1
            elif (index!=0):
                index = pnext[index-1]
            else:
                pnext[i] = 0
                i += 1
        return pnext

    
