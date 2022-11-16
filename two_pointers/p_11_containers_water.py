'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        i = 0
        j = n-1
        max_area = 0
        while i < j:

            new_area = (j - i) * min(height[i], height[j])

            if new_area >= max_area:
                max_area = new_area
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area
