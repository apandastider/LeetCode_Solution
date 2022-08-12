'''
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
'''

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ## non-optimized solution
#         carry = 0
        
#         ans = []
        
#         while num or k != 0:
#             if num:
#                 curr_digit = num.pop()
#             else:
#                 curr_digit = 0
                
#             adder = k % 10
#             k = k // 10
#             # print(k)
#             adder_res = adder + curr_digit + carry
            
#             carry = adder_res // 10
#             ans.insert(0, adder_res % 10)
            
#         if carry != 0:
#             ans.insert(0, carry)
#         # print(ans)
        
#         return ans

        string = ''
    
        for d in num:
            string += str(d)
        
        res = str(int(string) + k)
        
        ans = []
        
        for char in res:
            ans.append(int(char))
        return ans
                    
        
