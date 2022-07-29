'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = ListNode(0)
        q = p
        l3_ = []
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            while l1 != None or l2 != None:
                if l1 == None and l2!= None:
                    l3_.append(l2.val)
                    l2 = l2.next
                elif l2 == None and l1!= None:
                    l3_.append(l1.val)
                    l1 = l1.next
                elif l1.val <= l2.val:
                    l3_.append(l1.val)
                    l1 = l1.next
                elif l2.val <= l1.val:
                    l3_.append(l2.val)
                    l2 = l2.next
                
        for i in l3_:
            p.next = ListNode(i)
            p = p.next
            
        return q.next
                
