'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res = []

        def backtrack(curr, pos, total):

            if total == 0:
                res.append(curr.copy())

            if total <= 0:
                return

            prev = -1

            for i in range(pos, len(candidates)):

                if prev == candidates[i]:
                    continue
                
                curr.append(candidates[i])
                backtrack(curr, i + 1, total - candidates[i])
                curr.pop()

                prev = candidates[i]
        backtrack([], 0, target)

        return res
