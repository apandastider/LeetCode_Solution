'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ## I took help from discussion to know the technique of diagonal + reflect matrix for matric clockwise rotation
        ## when to do anti-clockwise rotation
        '''
        for i in range(len(matrix)):
            matrix[i].reverse()
        print(matrix)        
        '''
        
        # When to do clock-wise rotation
        '''
        matrix.reverse()
        print(matrix)
        '''
        
        matrix.reverse()
        
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
