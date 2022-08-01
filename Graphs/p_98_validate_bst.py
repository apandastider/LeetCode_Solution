'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

min_val = float('inf')

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.stack = []
        self.inOrderTraversal(root)
        
        for i in range(len(self.stack)-1):
            if self.stack[i] >= self.stack[i+1]:
                return False
        return True
        
        #         global min_val
#         # global stack
        
#         if root.left is None:
#             min_val = min(min_val, root.val)
#         if root.right is None:
#             min_val = min(min_val, root.val)
            
#         if root.left:
#             if root.left.val >= root.val:
#                 return False
#             else:
#                 min_val = min(min_val, root.val)
#                 self.isValidBST(root.left)
#         if root.right:
#             if root.right.val <= root.val:
#                 return False
#             else:
#                 min_val = min(min_val, root.val)
#                 self.isValidBST(root.right)
    def inOrderTraversal(self, node):
        
        if node.left:
            self.inOrderTraversal(node.left)
            
        self.stack.append(node.val)
        
        if node.right:
            self.inOrderTraversal(node.right)
        
        
