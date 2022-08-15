'''
Given an m x n matrix, return all elements of the matrix in spiral order.


'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        curr_row = 0
        curr_col = 0
        
        max_row = len(matrix)
        max_col = len(matrix[0])
        
        result = []
        
        while curr_row < max_row and curr_col < max_col:
            # print(result)
            for i in range(curr_col, max_col-curr_col):
                if matrix[curr_row][i] != "#":
                    result.append(matrix[curr_row][i])
                    matrix[curr_row][i] = "#"
            
            for i in range(curr_row + 1, max_row - curr_row):
                if matrix[i][max_col-curr_col-1] != "#":
                    result.append(matrix[i][max_col-curr_col-1])
                    matrix[i][max_col-curr_col-1] = "#"
            
            if curr_row < max_row:
                curr_row += 1
                
            if curr_col < max_col:    
                curr_col += 1
            
            for i in range(max_col - curr_col - 1, curr_col - 2, -1):
                if matrix[max_row-curr_row][i] != "#":
                    result.append(matrix[max_row-curr_row][i])
                    matrix[max_row-curr_row][i] = "#"
                
            for i in range(max_row - curr_row - 1, curr_row - 1, -1):
                if matrix[i][curr_col - 1] != "#":
                    result.append(matrix[i][curr_col - 1])
                    matrix[i][curr_col - 1] = "#"
                
        return result
            
            
                
        
        
