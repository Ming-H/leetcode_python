#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        N = len(digits)
        i = N-1
                
        while digits[i] == 9:
            digits[i] = 0
            
            if i == 0:
                digits.insert(0,1)
                return digits
            else:
                i -= 1
        
        digits[i] += 1
        return digits

