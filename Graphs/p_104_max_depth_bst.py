'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0

            
        if root is None:
            return self.depth
        else:
            stack = [root]
            while len(stack) != 0:
                # print("old_stack : ", stack)
                old_stack = stack.copy()
                self.depth += 1
                for _ in old_stack:
                    node = stack.pop(0)
                    # print("[Starting For loop]")
                    if node.left is not None: 
                        # print("Found Left")
                        stack.append(node.left)
                        # print(stack)
                    if node.right is not None:
                        # print("Found Right")
                        stack.append(node.right)
                        # print(stack)
                    # stack.pop(0)
                # print("curr_stack : ", stack)
                    
            return self.depth 
        
