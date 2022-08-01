'''
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

'''

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        if len(mat) == 1:
            return mat[0][0]
        
        sum_ = 0
        for i in range(len(mat)):
            sum_ += mat[i][i] + mat[i][len(mat)-1-i]
            
        if len(mat)%2 != 0:
            sum_ -= mat[len(mat)//2][len(mat)//2]
            return sum_
        else:
            return sum_
