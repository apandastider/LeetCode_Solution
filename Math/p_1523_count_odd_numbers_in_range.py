'''
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

'''

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if high - low == 2:
            if high%2 == 0:
                return 1
            else:
                return 2
        if high == low:
            if high%2 == 0:
                return 0
            else:
                return 1
        if high - low == 1:
            return 1
               
        difference_half = (high - low) / 2
        
        if low%2 != 0 and high%2 != 0:
            return int(difference_half) + 1
        if low%2 == 0 and high%2 == 0:
            return int(difference_half)
        if low%2 != 0 and high%2 == 0:
            return int(difference_half) + 1
        if low%2 == 0 and high%2 != 0:
            return int(difference_half) + 1
