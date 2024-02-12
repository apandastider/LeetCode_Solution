'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.


'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ''' my solution failes at testcase number 151/172 --> [1,2,0,1]
        if len(nums) == 1:
            return True
        i = len(nums) - 1
        j = len(nums) - 2
        flag = False
        
        while j >= 0:
            print(nums[j], i-j, i , j, flag)

            if nums[j] >= i-j:
                i -= 1
                j -= 1
                flag = True
            else:
                j -= 1
                flag = False

        return flag 

        '''
        ## more simple solution from Neetcode YT

        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):

            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False


        
