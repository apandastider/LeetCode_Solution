'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

'''


class Solution:
    def decodeString(self, s: str) -> str:
        
        ## my solution was on the same day, but I have to check discussion to code it :(
        nums_stack = []
        character_stack = []
        
        curr_num = 0
        curr_s = ''
        
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            
            elif char == '[':
                character_stack.append(curr_s)
                nums_stack.append(curr_num)
                curr_num = 0
                curr_s = ''
            elif char == ']':
                prev = character_stack.pop()
                prev_num = nums_stack.pop()
                
                curr_s = prev + prev_num*curr_s
            else:
                curr_s += char
        return curr_s
