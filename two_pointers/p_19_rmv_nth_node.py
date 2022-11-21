'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        slow = head
        fast = head

        if head.next is None and n == 1:
            return head.next

        for i in range(n):
            if fast.next is None:
                if i == n-1:
                    head = head.next
                    return head
            fast = fast.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        if slow.next is not None:
            slow.next = slow.next.next
        return head

                                                     

        
        
