'''
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.
'''




class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        if mat == target:
            return True
        
        # for clockwise rotation, first reverse by up-to-down order
        
        mat.reverse()
        for _ in range(4):
            
            # let's tranpose it now
            for i in range(len(mat)):
                for j in range(i, len(mat[0])):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            
            if mat == target:
                return True
            mat.reverse()
            
        return False  
