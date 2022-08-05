'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
'''

class Solution:
    def fib(self, n: int) -> int:
        
        ## Recursion, not DP slow
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
        
#         return self.fib(n-1) + self.fib(n-2)

        ## DP solution
#         f = [0, 1]
        
#         for i in range(2, n+1):
#             f.append(f[i-1]+f[i-2])
#         return f[n]

        f_0 = 0
        f_1 = 1
        
        for i in range(0,n):
            f_0, f_1 = f_1, f_0+f_1
        return f_0
        
