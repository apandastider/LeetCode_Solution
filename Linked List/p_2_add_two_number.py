'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr_sum = 0
        carry = 0
        res = []
        while l1 or l2:
            if l1 == None:
                curr_sum = carry + l2.val
                res.append(curr_sum % 10)
                carry = curr_sum // 10
                l2 = l2.next
            elif l2 == None:
                curr_sum = carry + l1.val
                res.append(curr_sum % 10)
                carry = curr_sum // 10
                l1 = l1.next
            
            else:
                curr_sum = carry + l1.val + l2.val
                res.append(curr_sum % 10)
                carry = curr_sum // 10
                l1 = l1.next
                l2 = l2.next
        
        if carry != 0:
            res.append(carry)
        if len(res) == 1:
            return ListNode(val = res[0])
        
        q = ListNode(val = res[len(res)-1])
        i = len(res) - 2
        
        while i >= 0:
            out = ListNode(val = res[i], next = q)
            q = out
            
            i -= 1
            
        return out
        
