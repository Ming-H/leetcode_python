#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        https://blog.csdn.net/qian2729/article/details/50741443"
        代码中用到了KMP算法用的部分匹配数组。
        给定字符串s，其反转字符串为rev_s，s + “#” + rev_s的部分匹配数组的最后
        一位共有元素长度就是反转字符串rev_s后缀和s前缀相同的部分的长度。之所以用
        ”#”，是为了在计算部分匹配数组时，可以将rev_s和s进行分离，使得他们连起来
        的字符串的前缀和后缀不会跨越这两个子字符串

        """
        rev_s = s[::-1]
        l = s + "#" +  rev_s
        p = [0] * len(l)
        for i in range(1,len(l)):
            j = p[i - 1]
            while j > 0 and l[i] != l[j]:
                j = p[j - 1]
            p[i] = j + (l[i] == l[j])
        return rev_s[:len(s) - p[-1]] + s

# @lc code=end

