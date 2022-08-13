'''
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        ## Could not solve by myself, oh! Recursion!! :( 
        def dfs(tree, linkedList):
            if linkedList is None:
                return True
            if tree is None:
                return False 
            
            return tree.val == linkedList.val and (dfs(tree.left, linkedList.next) or dfs(tree.right, linkedList.next))
        
        if head is None:
            return True
        
        if root is None:
            return False
        
        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        
        
        
