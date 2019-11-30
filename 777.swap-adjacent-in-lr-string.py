#
# @lc app=leetcode id=777 lang=python3
#
# [777] Swap Adjacent in LR String
#

# @lc code=start
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i, j = 0, 0
        if(start == end): 
            return True
        
        n = len(start)
        
        while i < n and j < n:
            while i < n - 1 and (start[i] == 'X'): i += 1
            while j < n -1 and (end[j] == 'X'): j += 1
            
            if (start[i] != end[j]): 
                return False
            if (start[i] == 'R' and j < i) or (start[i] == 'L' and i < j): 
                return False
            i += 1
            j += 1
            
        return True
# @lc code=end

