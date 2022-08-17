'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hash_map:
                hash_map[sorted_word] = [word]
            else:
                hash_map[sorted_word].append(word)
                
        return [val for val in hash_map.values()]
        
