'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 
'''

class Solution:
    def romanToInt(self, s: str) -> int:

        hash_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        j = 0
        val = 0
        while j < len(s):
            if s[j] == 'I':
                if j < len(s)-1 and s[j+1] == 'V':
                    val += 4
                    j += 2
                elif j < len(s)-1 and s[j+1] == 'X':
                    val += 9
                    j+= 2
                else:
                    val += 1
                    j += 1
            elif s[j] == 'X':
                if j < len(s)-1 and  s[j+1] == 'L':
                    val += 40
                    j += 2
                elif j < len(s)-1 and  s[j+1] == 'C':
                    val += 90
                    j+= 2
                else:
                    j += 1
                    val += hash_dict['X']
            elif s[j] == 'C':
                if j < len(s)-1 and  s[j+1] == 'D':
                    val += 400
                    j += 2
                elif j < len(s)-1 and  s[j+1] == 'M':
                    val += 900
                    j+= 2
                else:
                    j += 1
                    val += hash_dict['C']
            else:
                val += hash_dict[s[j]]
                j += 1
            # print(val)
        return val
                
        
