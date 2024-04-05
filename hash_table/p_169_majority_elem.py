'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count_dict = {}

        max_len = len(nums)/2

        out = 0

        for i in range(len(nums)):
            if nums[i] in count_dict.keys():
                count_dict[nums[i]] += 1
                if count_dict[nums[i]] > max_len:
                    out = nums[i]
            else:
                count_dict[nums[i]] = 1
                if count_dict[nums[i]] > max_len:
                    out = nums[i]
        
        return out
