'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## an Important code as it teaches on splitting, reversing and merging a Linked List
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        a , b = self.splitList(head)
        
        b = self.reverse(b)
        
        head = self.merge(a, b)
        
        # return head
        
    def splitList(self, head):
        
        fast = head
        slow = head
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next
            fast = fast.next
            
        middle = slow.next
        slow.next = None
        
        return head, middle
    
    def reverse(self, head):
        
        last = None
        curr = head
        
        while curr:
            next_ = curr.next
            curr.next = last
            last = curr
            curr = next_
            
        return last
    
    def merge (self, a, b):
        
        head = a 
        tail = a
        
        a = a.next
        
        while b:
            tail.next = b
            tail = tail.next
            b = b.next
            if a:
                a , b = b, a
                
        return head
