'''
A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic:

1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.

'''

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        count_l = 0
        count_r = 0
        
        ans = []
        
        while count_l < len(l) and count_r < len(r):
            flag = 0
            curr_list = nums[l[count_l]:r[count_r]+1]
            curr_list.sort()
            
            for i in range(len(curr_list)-2):
                if curr_list[i+1] - curr_list[i] != curr_list[i+2] - curr_list[i+1]:
                    flag = 1
                    break
                    
            if flag == 1:
                ans.append(False)
            else:
                ans.append(True)
            count_l += 1
            count_r += 1
        return ans
