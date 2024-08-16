'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.



'''

class Solution:
    def reverseWords(self, s: str) -> str:
        print(len(s))
        i = 0
        j = 0
        counter = 0
        flag = True

        res = ""

        while i < len(s):
            
            if not s[i].isspace():

                if flag == True:
                    j = i
                    flag = False
                
                counter += 1
                print(i,counter,j)

            if s[i].isspace() and counter != 0:
                res = ' '+s[j:j+counter]+res
                counter = 0
                flag = True

            i+= 1
        if s[len(s)-1].isspace():
            return res[1:]
        else:
            return s[j:j+counter]+res
