'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        j = 0
        
        lis = []
        
        while i <= len(word1) and j <= len(word2):
            
            if i == len(word1):
                lis.append(word2[j:])
                return ''.join(lis)
            if j == len(word2):
                lis.append(word1[i:])
                return ''.join(lis)
            
            lis.append(word1[i])
            lis.append(word2[j])
            i += 1
            j += 1
            
        return ''.join(lis)
