'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

'''



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ## my logic was quite similar to posted solution, just thought in a more complex way
        
        if numRows == 1 or numRows >=len(s):
            return s 
        
        list_ = ['']*numRows

        curr_indx = 0
        step = 1

        for char in s:
            list_[curr_indx] += char

            if curr_indx == 0:
                step = 1
            if curr_indx == numRows - 1:
                step = -1
            curr_indx += step

        return ''.join(list_)
