'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

'''

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        inc_flag = 0
        
        for idx in range(len(nums)-1):
            if nums[idx] <= nums[idx+1]:
                inc_flag = 0
            else:
                inc_flag = 1
                break
                
        dec_flag = 0
        for idx in range(len(nums)-1):
            if nums[idx] >= nums[idx+1]:
                dec_flag = 0
            else:
                dec_flag = 1
                break
        if inc_flag == 0 or dec_flag == 0:
            return True
        else:
            return False
            
