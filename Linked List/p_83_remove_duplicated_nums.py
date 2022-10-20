'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head is None:
            return head
            
        res = ListNode()
        res.next = ListNode(head.val)
        dummy = res.next
        
        while head is not None:

            if dummy.val != head.val:
                
                dummy.next = ListNode(head.val)
                dummy = dummy.next
                
            head = head.next
        
        return res.next
        
        
