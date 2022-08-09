'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        number1 = 0
        number2 = 0
        
        for c in num1:
            number1 = number1*10 + (ord(c)-48)
        
        for c in num2:
            number2 = number2*10 + (ord(c)-48)
        
        res_int = number1 * number2
        
        if res_int == 0:
            return str(0)
        res = ''
        list_nums = []
        
        
        while res_int:
            list_nums.append(str(res_int % 10))
            res_int = res_int // 10
        
        for _ in range(len(list_nums)):
            res += list_nums.pop()
            
        return res
