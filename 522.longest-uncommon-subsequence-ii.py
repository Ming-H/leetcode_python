#
# @lc app=leetcode id=522 lang=python3
#
# [522] Longest Uncommon Subsequence II
#

# @lc code=start
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        C = collections.Counter(strs)
        S = sorted(C.keys(), key = len, reverse = True)
        for i,s in enumerate(S):
            if C[s] != 1: 
                continue
            b = True
            for j in range(i):
                I, c = -1, True
                for i in s:
                    I = S[j].find(i,I+1)
                    if I == -1:
                        c = False
                        break
                if c:
                    b = False
                    break
            if b: 
                return len(s)
        return -1
# @lc code=end

