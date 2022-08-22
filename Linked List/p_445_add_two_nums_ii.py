'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        list_l1 = []
        list_l2 = []
        
        while l1:
            list_l1.append(l1.val)
            l1 = l1.next
        while l2:
            list_l2.append(l2.val)
            l2 = l2.next
            
        l1_len = len(list_l1) - 1
        l2_len = len(list_l2) - 1
        
        res = []
        carry = 0
        curr_sum = 0
        while l1_len >=0 or l2_len >= 0:
            
            if l1_len < 0:
                curr_sum = carry + list_l2[l2_len]
                res.append(curr_sum % 10)
                carry = curr_sum // 10
            if l2_len < 0:
                curr_sum = carry + list_l1[l1_len]
                res.append(curr_sum % 10)
                carry = curr_sum // 10
            if l2_len >= 0 and l1_len >= 0:
                
                curr_sum = carry + list_l1[l1_len] + list_l2[l2_len]
                res.append(curr_sum % 10)
                carry = curr_sum // 10    
            
            l1_len -= 1
            l2_len -=1
        if carry != 0:
            res.append(carry)
        q = ListNode(val = res[0])
        
        if len(res) == 1:
            return q
        i = 1
        while i < len(res):
            out = ListNode(val = res[i], next = q)
            q = out
            i += 1
        return out
        
        
