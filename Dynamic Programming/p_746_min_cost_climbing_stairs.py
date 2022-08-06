'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost_each_node = [0] * len(cost)
        
        cost_each_node[0] = cost[0]
        
        cost_each_node[1] = cost[1]
        i = 2
        for c in cost[2:len(cost)]:
            cost_each_node[i] = c + min(cost_each_node[i-1], cost_each_node[i-2])
            i += 1
        return min(cost_each_node[-1], cost_each_node[-2])
        
