'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

'''

class Solution:
    def toLowerCase(self, s: str) -> str:
        
        list_s = []
        for idx, each_s in enumerate(s):
            if each_s.isupper():
                list_s.append(chr(ord(each_s) + 32))
            else:
                list_s.append(each_s)
        return ''.join(list_s)
