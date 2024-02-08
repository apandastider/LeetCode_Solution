'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        perm = []

        counter = {n:0 for n in nums}

        for n in nums:
            counter[n] += 1

        # print(counter)

        def DFS():

            print(counter, perm, res)

            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in counter:
                if counter[n] > 0:
                    perm.append(n)
                    counter[n] -= 1

                    DFS()

                    counter[n] += 1

                    perm.pop()


        DFS()

        return res
