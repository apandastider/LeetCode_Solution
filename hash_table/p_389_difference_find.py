'''
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        add_s = 0
        add_t = 0
        
        for each_t in t:
            add_t += ord(each_t)
        for each_s in s:
            add_s += ord(each_s)
            
        return chr(add_t - add_s)