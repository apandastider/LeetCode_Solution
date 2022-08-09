'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        if s == t:
            return True
        
        list_s = [each_s for each_s in s]
        
        list_t = [each_t for each_t in t]
        
        i = 0
        
        j = 0
        while i < len(list_s) or j < len(list_t):
            if i < len(list_s):
                if list_s[i] == '#':
                    if i > 0:
                        list_s.pop(i)
                        list_s.pop(i-1)
                        i -= 1
                    else:
                        i += 1
                else:
                    i += 1
                    
            if j < len(list_t):
                if list_t[j] == '#':
                    if j > 0:
                        list_t.pop(j)
                        list_t.pop(j-1)
                        j -= 1
                    else:
                        j += 1
                else:
                    j += 1
        if len(list_s) >= 1:
            if list_s[0] == '#':
                list_s.pop(0)
        if len(list_t) >= 1:    
            if list_t[0] == '#':
                list_t.pop(0)
            
        return list_s == list_t
            
            
