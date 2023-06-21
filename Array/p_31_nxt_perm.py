'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        index = -1
        # scan from right to left for finding less number than the preceding value
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                index = i-1
                break

        if index == -1:
            nums_len = n - 1
            ind = 0
            while(ind<=nums_len):
                nums[ind], nums[nums_len] = nums[nums_len], nums[ind]
                ind += 1
                nums_len -= 1
            return
        j = 0
        for i in range(n-1, index, - 1):
            if nums[i] > nums[index]:
                j = i
                nums[j], nums[index] = nums[index], nums[j]
                break
        # reverse from j to last element 
        nums_len = n - 1
        ind = index + 1
        while(ind<=nums_len):
            nums[ind], nums[nums_len] = nums[nums_len], nums[ind]
            ind += 1
            nums_len -= 1

