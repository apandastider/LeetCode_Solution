'''
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(cost) > sum(gas):
            return -1

        else:
            diff = []

            for i in range(len(gas)):
                diff.append(gas[i]-cost[i])

            total = 0
            indx = -1
            for i in range(len(diff)):
                if (total+diff[i]) < 0:
                    total = 0
                    indx = - 1
                else:
                    if indx == -1:
                        indx = i
                    total += diff[i]
            return indx

        
        
