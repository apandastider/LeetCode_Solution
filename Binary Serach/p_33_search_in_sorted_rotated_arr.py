'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''

'''
1st solution: Does not work for all testcases [164/195]

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1
        left = 0
        right = len(nums) - 1
        pivot = -1
        while left <= right:

            
            mid = (left+right)//2
            
            if nums[mid] == target:
                return mid
            if mid-1 >= 0:
                if nums[mid] < nums[mid-1]:
                    pivot = mid
                    break
            if mid+1 <= len(nums)-1:
                if nums[mid] > nums[mid+1]:
                    pivot = mid
                    break

            if nums[left] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

            if right < 0 or right > len(nums) - 1 or left < 0 or left > len(nums) - 1:
                break
        print(pivot)
        if pivot == -1:
            test_array = nums
            flag = None
        else:    
            left_array = nums[:pivot+1]
            right_array = nums[pivot+1:]

            if target >= left_array[0] and target <= left_array[len(left_array)-1]:
                test_array = left_array
                flag = 0
            else:
                test_array = right_array
                flag = 1
        
        low = 0
        high = len(test_array)-1
        ind = -1
        print(test_array)
        if len(test_array) == 1:
            if test_array[0] == target:
                if flag is not None and flag == 1:
                    ind = pivot + 1
                else:
                    ind = 0
            return ind

        while low < high:
            mid = (low+high)//2
            
            if test_array[mid] == target:
                ind = mid
                if flag is not None and flag == 1:
                    ind = ind + pivot + 1 
                break
            if test_array[mid] < target:
                low = mid + 1
            if test_array[mid] > target:
                high = mid

        return ind

'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            ## search in left sorted portion

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            ## search in right sorted portion    
            else:
                if target  < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return - 1

