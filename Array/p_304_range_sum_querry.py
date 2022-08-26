'''
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.

'''

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.summ = matrix[:]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if  i == 0 and j == 0:
                    self.summ[i][j] = matrix[i][j]
                elif i == 0 and j != 0:
                    self.summ[i][j] = matrix[i][j]+self.summ[i][j-1]
                elif i != 0 and j == 0:
                    self.summ[i][j] = matrix[i][j]+self.summ[i-1][j]
                else:
                    self.summ[i][j] = matrix[i][j]+self.summ[i][j-1]+self.summ[i-1][j]-self.summ[i-1][j-1]
                    
                # print(i,j, matrix[i][j], self.summ[i][j])
        self.summ.insert(0,[0]*len(matrix[0]))
        self.sum = []
        for r in self.summ:
            r.insert(0 , 0)
            self.sum.append(r)
        # print(self.sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        left_col_sum = self.sum[row2][col1-1]
        
        upper_row_sum = self.sum[row1-1][col2]
        
        up_corner = self.sum[row1-1][col1-1]

        corner_sum = self.sum[row2][col2]
        
        return corner_sum - left_col_sum - upper_row_sum + up_corner


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
