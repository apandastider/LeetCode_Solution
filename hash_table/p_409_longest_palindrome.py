'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 '''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1        
        hash_map = {}
        
        for l in s:
            if l in hash_map.keys():
                hash_map[l] = hash_map[l] + 1
            if l not in hash_map.keys():
                hash_map[l] = 1
        
        max_odd = 0
        count = 0
        total = 0

        for vals in hash_map.values():
            total += vals
            if vals % 2 != 0:
                count += vals - 1
                if vals > max_odd:
                    max_odd = vals
            if vals %2 == 0:
                count += vals
        if max_odd != 0:
            return count + 1
        else:
            return count
