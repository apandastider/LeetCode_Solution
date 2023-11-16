'''
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)

        # print(node.val)
        # self.res.append(node.val)

        if self.first == None and self.prev.val > node.val:
            self.first = self.prev
            self.prev = node
            self.mid = node
        elif self.first is not None and self.prev.val > node.val:
            self.last = node
        else:
            self.prev = node

        self.inorder(node.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # self.res = []
        self.first = self.mid = self.last = None
        self.prev = TreeNode(val = -math.inf)
        if root.left == None and root.right == None:
            return

        self.inorder(root)

        if self.last is None:
            self.first.val, self.mid.val = self.mid.val, self.first.val
        if self.last is not None:
            self.first.val, self.last.val = self.last.val, self.first.val


        # print(self.res)
            
        
