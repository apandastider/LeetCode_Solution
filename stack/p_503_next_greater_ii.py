'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

'''

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        len_nums = len(nums)
        
        nums.extend(nums[:len(nums)-1])
        
        res = [-1] * len(nums)
        
        stack = []
        
        for idx, val in enumerate(nums):
            # print(val)
            while stack and stack[-1][1] < val:
                curr_val = stack.pop()
                res[curr_val[0]] = val
            
            stack.append([idx, val])
            
        return res[:len_nums]
