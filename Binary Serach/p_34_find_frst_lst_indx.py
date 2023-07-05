'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left_indx = -1
        right_indx = -1

        left = 0
        right = len(nums) - 1
        ## first search on left side of the array
        while left <= right:
            mid = (left+right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left_indx = mid
                right = mid - 1

        ## again search in right side of the array
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                right_indx = mid
                left = mid + 1

        return [left_indx, right_indx]
        
