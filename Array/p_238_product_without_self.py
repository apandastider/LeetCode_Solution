'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        postfix = 1

        output = len(nums) * [0]
        output[0] = prefix
        
        for i in range(len(nums)-1):
            prefix = prefix * nums[i]
            output[i+1] = prefix

        for j in range(len(nums)-1, 0,-1):
            postfix = postfix * nums[j]
            # if j >= 1:
            output[j-1] = output[j-1] * postfix

        return output
