'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## This solution did not produce an optimized result!! :( 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_path = []
        
        self.q_path = []
        
        self.validPath(root, p.val, self.p_path)
        self.validPath(root, q.val, self.q_path)
        
        print(self.p_path, self.q_path)
        i = 0
        j = 0
        min_anc = []
        
        while i < len(self.p_path) and j < len(self.q_path):
            
            if self.p_path[i] == self.q_path[j]:
                min_anc.append(self.p_path[i])
            
            i += 1
            j += 1
        return TreeNode(min_anc[-1])      
    
    def validPath(self, tree, n1, path):
        if tree is None:
            return False
        
        path.append(tree.val)
        
        if tree.val == n1:
            path.append(tree.val)
            return True
        
        if self.validPath(tree.left, n1, path) or self.validPath(tree.right, n1, path):
            return True
        path.pop()
        
        
        
