'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            ## pop left first element currently in the array
            curr = nums.pop(0)

            perms = self.permute(nums)

            for perm in perms:

                perm.append(curr)
                
            
            result.extend(perms)

            nums.append(curr)

        return result
        
