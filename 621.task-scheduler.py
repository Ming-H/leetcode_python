#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        output = [0]*26
        for i in tasks:
            output[ord(i)-ord('A')] = output[ord(i)-ord('A')]+1
 
        count = 0
        max_o = max(output)
        for i in output:
            if i==max_o:
                count = count+1
                    
        return max(len(tasks), (max_o-1)*(n+1)+count)


# @lc code=end

