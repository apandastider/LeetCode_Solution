'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda i : i[0])

        result = []

        result.append(intervals[0])
        indx = 0
        for i in range(len(intervals)):

            if result[indx][1] >= intervals[i][0]:
                result[indx][1] = max(intervals[i][1], result[indx][1])

                if result[indx][0] >= intervals[i][0]:
                    result[indx][0] = min(intervals[i][0], result[indx][0])

            else:
                result.append(intervals[i])
                indx += 1

        return result

        
