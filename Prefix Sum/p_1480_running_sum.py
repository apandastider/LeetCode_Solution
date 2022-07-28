'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.


Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

'''

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if i == 0:
                prev_sum = nums[i]
                res.append(nums[i])
            else:
                prev_sum = nums[i] + prev_sum
                res.append(prev_sum)
        return res
      
      
