#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """
        O(n^2) time
        O(1) memory
        """
        n,m=len(A),len(B)
        res=0    
        for offset in range(-m,n):
            i,j=max(offset,0),max(0,-offset)
            cur=0
            while i<n and j<m:
                if A[i]==B[j]:
                    cur+=1
                    res=max(res,cur)
                else:
                    cur=0
                i+=1
                j+=1
        return res


# @lc code=end

