'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
#         s = ''
        
#         for i in range(len(digits)):
#             s = s + str(digits[i])
        
#         int_s = int(s) + 1
#         out_s = str(int_s)
#         out = []
        
#         for i in range(len(out_s)):
#             out.append(int(out_s[i]))
        num = 0
        for i in range(len(digits)):
            num = num*10 + digits[i]
        out = [int(i) for i in str(num + 1)]
    
        return out
