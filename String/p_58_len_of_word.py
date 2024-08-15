'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_rev = s[::-1]
        flag = 0
        count = 0
        for i in range(len(s_rev)):
            if s_rev[i].isspace() and flag == 0:
                continue
            else:
                flag = 1
                if s_rev[i].isspace() != True:
                    count += 1
                else:
                    break
        return count

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        res = 0
        flag = False
        for i in range(len(s)-1,-1,-1):
            # print(i)
            if s[i] == ' ' and flag == True:
                break
            
            if s[i] != ' ':
                flag = True
                res += 1

        return res
