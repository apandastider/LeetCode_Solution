'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        self.res = []
        
        if root is None:
            return self.res
        
        self.helper(root)

        return self.res

    def helper(self, node):
        if node.left:
            self.helper(node.left)
    
        self.res.append(node.val)
        
        if node.right:
            self.helper(node.right)
        
