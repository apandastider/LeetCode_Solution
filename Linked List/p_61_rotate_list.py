'''
Given the head of a linked list, rotate the list to the right by k places.


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
    ## I wrote a non-optimized code at first which could not optimize large inputs, later changed it looking into  
    
        if head is None:
            return None
        if head.next is None:
            return head
        
        curr_node = head
        
        length = 1
        
        while curr_node.next:
            curr_node = curr_node.next
            length += 1
            
        curr_node.next = head
        
        break_pnt = length - (k % length)
        
        while break_pnt > 0:
            curr_node = curr_node.next
            break_pnt -= 1
            
        newHead = curr_node.next
        curr_node.next = None
        
        return newHead
