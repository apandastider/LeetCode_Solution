'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_s = {}
        hash_t = {}
        
        for each in s:
            if each in hash_s:
                hash_s[each] += 1
            else:
                hash_s[each] = 1
                
        for each in t:
            if each in hash_t:
                hash_t[each] += 1
            else:
                hash_t[each] = 1
        
        
#         for keys in hash_t.keys():
#             if keys not in hash_s:
                
#                 return False
#             else:
#                 if hash_s[keys] != hash_t[keys]:
#                     return False
                
#         return True
        return hash_s == hash_t
                
        
