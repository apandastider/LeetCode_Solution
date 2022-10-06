'''
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ## Need to understand the DP solution from Youtube Tutorials! Started Coding after ICRA deadline
        ''' Complete DP Solution which suffered from TLE
        n = len(s)
        dp_mat = [[0 for i in range(n)] for j in range(n)]

        ## for substring length 1
        for i in range(n):
            dp_mat[i][i] = 1
        max_len = 1
        
        ## for substring length 2
        start = 0
        for i in range(n-1):
            if s[i] == s[i+1]:
                start = i
                dp_mat[i][i+1] = 1
                max_len = 2

        ## for substring length 3
        k = 3
        while k <= n:
            ## declare start index
            i = 0
            ## loop through end index
            while i < n-k+1:
                j = i + k -1

                if dp_mat[i+1][j-1] == 1 and s[i] == s[j]:
                    dp_mat[i][j] = 1
                    
                    if k > max_len:
                        start = i
                        max_len = k

                i += 1

            k = k + 1

        return s[start:start+max_len]
        '''
        res = ""
        for i in range(len(s)):
            tmp = self.helper(s,i,i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.helper(s,i,i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l -= 1 
            r += 1
        return s[l+1:r]
        
