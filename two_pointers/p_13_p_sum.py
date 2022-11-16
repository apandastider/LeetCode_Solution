'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

'''

## This is not an optimized solution

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        all_zero = False
        
        for i in range(len(nums)):
            if nums[i] == 0:
                all_zero = True 
            else:
                all_zero = False
                break
        if all_zero:
            return [[0,0,0]]

        for i in range(len(nums)):

            j = 0
            k = len(nums) - 1
            while j < i and i < k:
                if nums[j] + nums[i] + nums[k] == 0:
                    list_res = [nums[j], nums[i], nums[k]]
                    # list_res.sort()
                    # print(list_res)
                    if list_res not in res:
                        res.append(list_res) 
                    j += 1
                    k -= 1      
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return res
