'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        dictionary = {}
        
        l = 0
        maxOcc = 0
        
        for r in range(len(s)):
            if s[r] not in dictionary:
                dictionary[s[r]] = 1
            else:
                dictionary[s[r]] += 1
            maxOcc = max(maxOcc, dictionary[s[r]])
            if r - l + 1 > maxOcc + k:
                dictionary[s[l]] -= 1
                l += 1
            
        return len(s) - l
