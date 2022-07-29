'''

Given the head of a singly linked list, reverse the list, and return the reversed list.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
#         while head.next != None:
#             res.append(head.val)
#             head = head.next
#         res.append(head.val)
        
#         res.reverse()
        
#         p = ListNode(res[0])
#         q = p
#         for i in range(1, len(res)):
#             p.next = ListNode(res[i])
#             p = p.next
        
#         return q
        result = ListNode(val = head.val)
        
        head = head.next
        q = None
        
        while head != None:
            q = ListNode(val = head.val, next = result)
            result = q
            head = head.next
        
        return q
                
