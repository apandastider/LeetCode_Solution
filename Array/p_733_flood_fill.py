'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
'''

## Satisfaction :D

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        self.visited_nodes = {}
        
        self.num_rows = len(image)
        self.num_cols = len(image[0])
        
        return self.helper(image, sr, sc, color)
        
    def helper(self, image, sr, sc, color):
        if (sr, sc) not in self.visited_nodes:
            self.visited_nodes[(sr,sc)] = 'True'
        ## move up
        
        if sr > 0 and sr < self.num_rows:
            curr_sr, curr_sc = sr - 1, sc
            if image[sr][sc] == image[curr_sr][curr_sc]:
                if (curr_sr, curr_sc) not in self.visited_nodes:
                    self.helper(image, curr_sr, curr_sc, color)
                    image[curr_sr][curr_sc] = color

        ## move down
        if sr >= 0 and sr < self.num_rows - 1:
            curr_sr, curr_sc = sr + 1, sc
            if image[sr][sc] == image[curr_sr][curr_sc]:
                if (curr_sr, curr_sc) not in self.visited_nodes:
                    self.helper(image, curr_sr, curr_sc, color)
                    image[curr_sr][curr_sc] = color
            
        ## move left
        if sc > 0 and sc < self.num_cols:
            curr_sr, curr_sc = sr, sc - 1
            if image[sr][sc] == image[curr_sr][curr_sc]:
                if (curr_sr, curr_sc) not in self.visited_nodes:
                    self.helper(image, curr_sr, curr_sc, color)
                    image[curr_sr][curr_sc] = color
        
        ## move right
        if sc >= 0 and sc < self.num_cols - 1:
            curr_sr, curr_sc = sr, sc + 1 
            if image[sr][sc] == image[curr_sr][curr_sc]:
                if (curr_sr, curr_sc) not in self.visited_nodes:
                    self.helper(image, curr_sr, curr_sc, color)
                    image[curr_sr][curr_sc] = color
    
        image[sr][sc] = color
        
        
        
        return image

