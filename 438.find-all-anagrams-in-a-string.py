#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def match(c1, c2):
            for k in c1:
                if k not in c2 or c1[k] != c2[k]:
                    return False
            return True
        
        pc = collections.Counter(p)
        sc = collections.Counter(s[0: len(p)])
        i = len(p)
        ret = list()
        while i < len(s):
            if match(pc, sc):
                ret.append(i-len(p))
            sc[s[i-len(p)]] -= 1
            sc[s[i]] = sc.get(s[i], 0) + 1
            i += 1
        if match(pc, sc):
            ret.append(i-len(p))
        return ret
# @lc code=end

