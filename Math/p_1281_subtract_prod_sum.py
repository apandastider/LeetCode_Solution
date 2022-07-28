'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
'''

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add = 0
        prod = 1
        
        while n != 0:
            rem = n % 10
            n = n // 10
            add = add + rem
            prod = prod * rem
            
        return prod - add
