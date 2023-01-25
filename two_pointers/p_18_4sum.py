'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

'''

# took help from discussion to solve this task

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        if len(nums) < 4:
            return res
        else:
            nums.sort()
            
            for i in range(len(nums)-3):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                for j in range(i+1, len(nums)-2):
                    if j > i+1 and nums[j] == nums[j-1]:
                        continue
                    left = j+1
                    right = len(nums)-1

                    while left < right:

                        summ = nums[i]+nums[j]+nums[left]+nums[right]
                        
                        if summ == target:
                            res.append([nums[i], nums[j], nums[left], nums[right]])
                            left += 1
                            right -= 1
                            while left < right and nums[left] == nums[left-1]:
                                left += 1
                            while left < right and nums[right] == nums[right + 1]:
                                right -= 1
                        if summ > target:
                            right -=1 
                        elif summ < target:
                            left += 1
            return res
        
        

