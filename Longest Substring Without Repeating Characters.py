# -*- coding:utf-8 -*-
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a 
substring, "pwke" is a subsequence and not a substring.

"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        Longstring = []
        current = []
        for i in range(len(s)):
            if s[i] not in current:
                current.append(s[i])
                if len(Longstring) < len(current):
                    Longstring = current
            else:
                current = []
        Longstring = ''.join(Longstring)
        return Longstring
        
if __name__ == "__main__":
    s = "abcabcbb"
    method = Solution()
    result = method.lengthOfLongestSubstring(s)
    print(result)
