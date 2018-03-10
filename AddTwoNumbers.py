# -*- coding:utf-8 -*-
"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        L1 = list(map(int, l1.strip().split('->')))
        L2 = list(map(int, l2.strip().split('->')))
        if len(L1) > len(L2):
            for i in range(len(L1)-len(L2)):
                L2.append(0)
        if len(L2) > len(L1):
            for i in range(len(L2)-len(L1)):
                L1.append(0)
        print(L1,L2)
        L = []
        flag =False
        for x,y in zip(L1,L2):
            print('x,y is',x,y)
            current = x+y
            if flag == True:
                current += 1
            if current > 9:
                L.append(current%10)
                flag = True
            else:
                L.append(current)
                flag = False
        return L
    
    # https://leetcode.com/problems/add-two-numbers/discuss/1102/Python-for-the-win
    def addTwoNumbers(self, l1, l2):  
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n / 10)
            return node
        return tolist(toint(l1) + toint(l2))
        
    #Iterative tolist instead of recursive:
    def addTwoNumbers(self, l1, l2):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        n = toint(l1) + toint(l2)
        first = last = ListNode(n % 10)
        while n > 9:
            n /= 10
            last.next = last = ListNode(n % 10)
        return first
                
if __name__ == "__main__":
    l1 = "2 -> 4 -> 3"
    l2 = "5 -> 6 -> 4"
    method = Solution()
    result = method.addTwoNumbers(l1,l2)
    print(result)
                
                
                
                
                
           
            
