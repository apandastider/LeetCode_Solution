'''
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        
        Not an optimized Code!
        
        counter = 0
        
        for i in range(len(nums)):
            prod = 1
            right_ind = i
            while right_ind < len(nums):
                prod = prod * nums[right_ind]
                
                if prod < k:
                    counter += 1
                else:
                    break
                
                right_ind += 1
                
        return counter
        '''
        if k <= 1:
            return 0
        
        prod = 1
        counter = left_indx = 0
        
        for right_indx, val in enumerate(nums):
            prod *= val
            
            while prod >= k:
                prod /= nums[left_indx]
                left_indx += 1
            if prod < k:
                counter += right_indx - left_indx + 1
        return counter
        
