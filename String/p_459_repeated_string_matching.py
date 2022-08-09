'''
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        half_len = len(s)//2
        curr_s = ''
        for idx, c in enumerate(s[:half_len]):
            curr_s += c
            
            if len(s) % len(curr_s) == 0:
                if curr_s * (len(s) // len(curr_s)) == s:
                    return True
        
        return False
