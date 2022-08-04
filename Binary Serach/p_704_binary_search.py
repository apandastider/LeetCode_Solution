'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
            
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = int((low + high) / 2)
            guess = nums[mid]
            if target == guess:
                return mid
            if target < guess:
                high = mid - 1
            if target > guess:
                low = mid + 1
        return -1
