'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()

        closest_sum = math.inf

        for i in range(len(nums)-1):
            ptr1 = i + 1
            ptr2 = len(nums)-1

            while ptr1 < ptr2:
                sum_ = nums[ptr1] + nums[i] + nums[ptr2]

                if abs(target-sum_) < abs(target-closest_sum):
                    closest_sum = sum_
                
                if sum_ > target:
                    ptr2 -= 1
                else:
                    ptr1 += 1

        return closest_sum

        

        
