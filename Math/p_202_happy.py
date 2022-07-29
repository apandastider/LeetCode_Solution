'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

'''

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        summ = 0
        for i in str(n):
            summ = summ + int(i)
        if summ == 1:
            return True
        
        checker = self.getSquared(n)
        
        if checker > 1 and checker <=9:
            checker = self.getSquared(checker)
        
        while checker // 10 != 0:
            checker = self.getSquared(checker)
            if checker == 1:
                return True
        return False
        
    def getSquared(self,num: int) -> int:
        add = 0
        for i in str(num):
            add = add + int(i) ** 2
        return add
        
        
        
