'''
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
'''


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        string = list(str(n))
        
        ## algorithm implementation of next-permutation
        
        i = j = len(string) - 1
        
        while i > 0 and string[i-1] >= string[i]:
            i -= 1
            
        if i == 0:
            res = ''.join(reversed(string))
            return int(res) if n < int(res) < 2**31 - 1 else -1
        
        pivot = i - 1
                
        while string[j] <= string[pivot]:
            j -= 1
                    
        string[j], string[pivot] = string[pivot], string[j]
                
        res = ''.join(string[:i]) + ''.join(list(reversed(string[i:])))
        
        return int(res) if n < int(res) <= 2**31 - 1 else -1
        
