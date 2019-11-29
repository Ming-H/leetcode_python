#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Definition for singly-linked list.
        dummy=ListNode(0)
        dummy.next=head
        slow=fast=dummy
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                fast=dummy
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow 
        return  None     

# @lc code=end

