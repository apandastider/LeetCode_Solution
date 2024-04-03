'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        counter = 0

        for i in range(len(nums)):
            if nums[i] == val:
                counter += 1
        i = 0
        j = i + 1

        while i < len(nums):
            j = i + 1
            # print(j)
            if nums[i] == val:
                # print(i)
                while j < len(nums):

                    if nums[j] != val:
                        nums[i], nums[j] = nums[j], nums[i]
                        # print(j)
                        break
                    else:
                        j += 1
            
            i += 1
            

        return len(nums) - counter
        
