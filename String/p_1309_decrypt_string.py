'''
You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.
'''

class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        map_ = {}
        asci = 97
        for i in range(1,27):
            if i < 10:
                map_[str(i)] = chr(asci)
            else:
                map_[str(i)+'#'] = chr(asci)
            asci += 1
        
        list_hash = []
        
        j = len(s) - 1
        while j >= 0:
            
            if s[j] == '#':
                list_hash.append(s[j-2:j+1])
                j -= 3
            else:
                list_hash.append(s[j])
                j -= 1
        list_hash.reverse()
        
        s = ''
        for element in list_hash:
            
            s += map_[element]
            
        return s
