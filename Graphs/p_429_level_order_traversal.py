'''
Given an n-ary tree, return the level order traversal of its nodes' values.


'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if root is None:
            return []
        
        stack = [root]
        
        ans = []
        
        while stack:
            
            curr_list = []
            
            for i in range(len(stack)):
                curr_node = stack.pop(0)
                curr_list.append(curr_node.val)
                if curr_node.children:
                    for child in curr_node.children:
                        stack.append(child)
            ans.append(curr_list)
            
        return ans
                
