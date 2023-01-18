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
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

'''


class Solution:
    def intToRoman(self, num: int) -> str:

        ans = ''

        divider = [1000, 500, 100, 50, 10, 5, 1]
        sym = ['M','D', 'C', 'L', 'X', 'V', 'I']

        for i in range(len(divider)):
            rem = num % divider[i]
            div = num // divider[i]

            if div != 0:
                if i == 0:
                    ans += div * sym[i]
                if i == 1:
                    if rem // 400 == 1:
                        ans += 'CM'
                        rem = rem % 400
                    else:
                        ans += div * sym[i]
                if i == 2:
                    if rem // 400 == 1:
                        ans += 'CD'
                    elif div == 4:
                        ans += 'CD'
                    else:
                        ans += div * sym[i]
                if i == 3:
                    if rem // 40 == 1:
                        ans += 'XC'
                        rem = rem % 40
                    else:
                        ans += div * sym[i]
                if i == 4:
                    if rem // 40 == 1:
                        ans += 'XL'
                    elif div == 4:
                        ans += 'XL'
                    else:
                        ans += div * sym[i]
                if i == 5:
                    if rem // 4 == 1:
                        ans += 'IX'
                        rem = 0
                        div = 0
                    if div == 1:
                        ans += 'V'
                if i == 6:
                    if div == 4:
                        ans += 'IV'
                    else:
                        ans += div * sym[i]
                

            num = rem

        return ans
        
