'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        list_of_heads = []
        
        
        while head!= None:
            
            list_of_heads.append(head.val)
            head = head.next
            
        if len(list_of_heads) == 1:
            return ListNode(list_of_heads[0])
        
        if len(list_of_heads) == 2:
            return ListNode(list_of_heads[1])
        
        mid_val_idx = int(len(list_of_heads)/2)
        q = ListNode(val = list_of_heads[-1])
        out = None
        for j in range(len(list_of_heads)-2, mid_val_idx-1, -1):
            out = ListNode(val = list_of_heads[j], next = q)
            q = out
        return out    
        
