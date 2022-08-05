'''
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.summ = 0
        return self.helper(root)
        
    def helper(self, node):
        if node.left:
            if node.left.left is None and node.left.right is None:
                self.summ += node.left.val
            self.helper(node.left)
        if node.right:
            self.helper(node.right)
        return self.summ
        
