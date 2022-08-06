'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

'''


### Tried many solutions, but need to take help!! 
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        dictP = Counter(p)
        dictS = Counter(s[:len(p)])
        
        ans = []
        
        i = 0
        j = len(p)
        
        while j <= len(s):
            if dictP == dictS:
                ans.append(i)
            dictS[s[i]] -= 1
            if dictS[s[i]] <= 0:
                dictS.pop(s[i])
            if j < len(s):
                dict[s[j]] += 1
            i += 1
            j += 1
        return ans
        
