'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

'''

### Followed youtube tutorial to solve the problem

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []

        result = []

        def backtrack(openP, closeP):

            if openP == closeP == n:
                result.append("".join(stack))
                return

            if openP < n:
                stack.append("(")
                backtrack(openP+1, closeP)
                stack.pop()

            if openP > closeP:
                stack.append(")")
                backtrack(openP, closeP+1)
                stack.pop()

        backtrack(0,0)
        return result
