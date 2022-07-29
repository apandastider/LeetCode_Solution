'''
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

'''
## Given a sorted array, no required to run the merge_sort here. I practised it for my learning purposes

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        self.merge_sort(arr)
        for i in range(len(arr)-2):
            first = arr[i] - arr[i+1]
            second = arr[i+1] - arr[i+2]
            
            if first != second:
                return False
        return True
            
        
    def merge_sort(self, arr:List[int]):
        if len(arr) > 1:
            ## dividing into two parts
            left_arr = arr[:len(arr)//2]
            right_arr = arr[len(arr)//2:]
            ## recursion
            self.merge_sort(left_arr)
            self.merge_sort(right_arr)
            
            ## merge function
            
            i = 0
            j = 0
            k = 0
            
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1
