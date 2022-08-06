'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''

lass Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        all_paths = [[1 for cols in range(n)] for rows in range(m)]
        
        for rows in range(1, m):
            for cols in range(1, n):
                
                all_paths[rows][cols] = all_paths[rows-1][cols] + all_paths[rows][cols-1]
                
        return all_paths[m-1][n-1]
