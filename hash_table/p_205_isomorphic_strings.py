'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

'''

## here a hash map based solution has been provided 

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            hash_map = {}
            for i in range(len(s)):
                if hash_map != s[i]:
                    if t[i] not in hash_map.values():
                        hash_map[s[i]] = t[i]
                    if t[i] in hash_map.values() and s[i] not in hash_map.keys():
                        hash_map[s[i]] = " "
                    
            
            check = ""
            for j in range(len(s)):
                check = check + hash_map[s[j]]
            if check == t:
                return True
