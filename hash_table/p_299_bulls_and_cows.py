'''
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.
'''

from collections import Counter, OrderedDict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        dictS = Counter(secret)
        # print(dictS)
        bulls = 0
        cows = 0
        
        for idx, char in enumerate(guess):
            if char in dictS:
                if char == secret[idx]:
                    bulls += 1
                    dictS[char] -= 1
                    if dictS[char] <= 0:
                        dictS.pop(char)
        print(dictS)
        for idx, char in enumerate(guess):
            if char in dictS:
                if char != secret[idx]:
                    cows += 1
                    dictS[char] -= 1
                    if dictS[char] <= 0:
                        dictS.pop(char)
                
        return str(bulls)+'A'+ str(cows)+'B'
