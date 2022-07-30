'''

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

'''

# I solved it at first through brut force method, but it can be easily solved by prefix sum.

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
        sum_ = 0
        
        self.arr = [0] * len(self.nums)
        for i in range(len(self.nums)):
            self.arr[i] = sum_ + self.nums[i]
            sum_ = self.arr[i]
        
    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            return self.arr[right]-self.arr[left-1]
        else:
            return self.arr[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
