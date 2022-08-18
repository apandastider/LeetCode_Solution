'''
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

 
'''


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        if n <= 1:
            return 0
        
        hash_map = {}
        
        for idx, parent in enumerate(manager):
            if parent not in hash_map:
                hash_map[parent] = [idx]
            else:
                hash_map[parent].append(idx)
        
        print(hash_map)
        q = [[headID, informTime[headID]]]
             
        res = 0
        
        while q:
            curr_manager, curr_time = q.pop(0)
        
            res = max(res,curr_time)
             
            for child in hash_map[curr_manager]:
                if informTime[child] != 0:
                    q.append([child, curr_time + informTime[child]])
        return res
