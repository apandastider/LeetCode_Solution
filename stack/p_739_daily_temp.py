'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []
        
        for idx, t in enumerate(temperatures):
            
            while stack and stack[-1][0] < t:
                temp = stack.pop()
                res[temp[1]] = idx - temp[1] 
            
            stack.append([t, idx])
        
        return res
