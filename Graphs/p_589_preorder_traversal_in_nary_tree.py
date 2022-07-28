'''
589. N-ary Tree Preorder Traversal

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

'''

## solution through implementing DFS in preorder traversal


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        
        self.ans = []
        if root is None:
            return self.ans
        self.traversal(root)
        
        return self.ans
        
    def traversal(self, node):
        
        self.ans.append(node.val)
        
        while len(node.children) != 0:
            self.traversal(node.children.pop(0))
