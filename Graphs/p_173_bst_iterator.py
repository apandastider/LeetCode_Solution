'''
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.root = root
        self.list_nodes = []
        self.inOrder(root)
        
        self.list_nodes.insert(0, self.list_nodes[0]-1)
        self.pointer = 0
        
    def next(self) -> int:
        
        self.pointer += 1
        return self.list_nodes[self.pointer]

    def hasNext(self) -> bool:
        next_pointer = self.pointer + 1
        
        if next_pointer < len(self.list_nodes):
            return True
        else:
            return False
    
    def inOrder(self, node):
        
        if node.left is not None:
            self.inOrder(node.left)
        
        self.list_nodes.append(node.val)
        
        if node.right is not None:
            self.inOrder(node.right)
    
        # self.list_nodes.append(node.val)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
