'''
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.

'''

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        add = 0
        if len(arr)%2 != 0:
            add += sum(arr)
            
        add += sum(arr)
        
        odd_index = []
        
        for i in range(1, len(arr), 2):
            odd_index.append(i)
        for j in range(1, len(odd_index)):
            for i in range(len(arr)):
                if i + odd_index[j] <= len(arr):
                    add += sum(arr[i:i+odd_index[j]])
        
        return add
