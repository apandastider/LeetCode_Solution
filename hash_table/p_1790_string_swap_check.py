'''
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
'''

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if s1 == s2:
            return True
        hash_s1 = {}
        hash_s2 = {}

        violation_count = 0

        count = 0
    
        for s1_, s2_ in zip(s1, s2):
            if s1_ != s2_:
                violation_count += 1            
                hash_s1[s1_] = count
                hash_s2[s2_] = count
            count += 1
        if hash_s1.keys() == hash_s2.keys() and len(hash_s1.keys()) == 2 and violation_count == 2:
            return True
        # return violation_count == 2
