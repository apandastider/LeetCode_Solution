'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None or (root.left is None and root.right is None):
            return True
        l = self.calcDepth(root.left)
        r = self.calcDepth(root.right)
        if abs(r - l) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
        
    
    def calcDepth(self, node):
        
        if node is None:
            return 0
        
        # if node.left is None and node.right is None:
        #     return 1
        
        return max(self.calcDepth(node.left), self.calcDepth(node.right)) + 1
        
