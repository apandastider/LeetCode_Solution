'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        if head.next is None:
            return head

        temp = head

        while temp is not None and temp.next is not None:

            if temp.val != temp.next.val:

                temp.val, temp.next.val = temp.next.val, temp.val

            temp = temp.next.next

        return head

        
