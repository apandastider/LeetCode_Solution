'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

'''

## I wen through discussions for getting help for this code

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        zero_idx = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                zero_idx += 1
