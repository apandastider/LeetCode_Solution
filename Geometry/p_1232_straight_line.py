'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates) == 1:
            return False
        prev_slope = 0
        curr_slop = 0
        
        x_flag = 1
        for i in range(len(coordinates)-1):
            if coordinates[i][0] != coordinates[i+1][0]:
                x_flag = 0
                break
        if x_flag == 1:
            return True
        
        y_flag = 1
        for i in range(len(coordinates)-1):
            if coordinates[i][1] != coordinates[i+1][1]:
                y_flag = 0
                break
        if y_flag == 1:
            return True
        
        for i in range(len(coordinates)-1):
            num = coordinates[i+1][1]-coordinates[i][1]
            den = coordinates[i+1][0]-coordinates[i][0]
            if den == 0:
                return False
            curr_slop = -num/den
            if i == 0:
                prev_slop = curr_slop
            if prev_slop != curr_slop:
                return False
        return True
        
