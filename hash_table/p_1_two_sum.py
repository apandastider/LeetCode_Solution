'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''

## I provided here a hash map based solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}
        
        for idx, value in enumerate(nums):
            hash_map[value] = idx
        ans1 = None
        ans2 = None
        # counter = 0
        for idx, value in enumerate(nums):
            if (target-value) in hash_map:
                if idx != hash_map[target-value]:
                    ans1, ans2 = idx, hash_map[target-value]
        return [ans1, ans2]
