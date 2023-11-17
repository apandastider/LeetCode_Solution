'''
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

[I took guidance from Youtube to solve this problem]
'''

class Solution:
    def numTrees(self, n: int) -> int:
        ## base case : numTrees(0) -> 1, numTrees(1) -> 1
        valid_bst = [1] * (n+1)

        for nodes in range(2, n+1):
            total_tree = 0
            for root in range(1, nodes+1):
                left_stree = root - 1
                right_stree = nodes - root
                total_tree += valid_bst[left_stree] * valid_bst[right_stree]
            valid_bst[root] = total_tree

        return valid_bst[n]
        
