
'''
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

'''

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ## 1st solution I derived! 
        dictWords = Counter(words)
#         print(dictWords)
#         curr_k = 0
#         list_words = []
            
#         old_max = 0
        
#         for _ in range(len(dictWords.keys())):
            
#             key = max(dictWords, key = dictWords.get)
#             list_words.append(key)
#             print(list_words)
#             curr_max = dictWords[key]
            
#             if old_max == curr_max:
#                 print(key)
#                 if key < list_words[-2]:
#                     list_words[-1], list_words[-2] = list_words[-2], list_words[-1]
                    
#             old_max = curr_max
#             dictWords.pop(key)
            
#         # print(list_words)
#         return list_words[:k]

        ## solution with heap
    
        word_count = [(-counter, word) for word, counter in dictWords.items()]
        
        heapq.heapify(word_count)
        
        return [heapq.heappop(word_count)[1] for _ in range(k)]
            
            
