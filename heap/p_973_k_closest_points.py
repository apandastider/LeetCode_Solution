'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        stack = []
        
        for point in points:
            dist = point[0]**2 + point[1]**2
            
            stack.append([dist, point])
            
        heapq.heapify(stack)
        
        count = 0
        
        ans = []
        
        while count < k:
            curr_low = heapq.heappop(stack)
            ans.append(curr_low[1])
            count += 1
        return ans
