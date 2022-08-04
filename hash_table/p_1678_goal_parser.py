'''
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.
'''

class Solution:
    def interpret(self, command: str) -> str:
        hash_map = {'G' : 'G', '()' : 'o', '(al)' : 'al'}
        
#         i = 0
        
#         s = '' 
        
#         while i < len(command):
#             print(i)
#             if command[i] == 'G':
#                 s += 'G'
#                 i += 1
#             elif command[i] == '(' and command[i+1] == ')':
#                 s += hash_map['()']
#                 i += 2
#             elif command[i] == '(' and command[i+1] == 'a':
#                 s += hash_map['(al)']
#                 i += 4
#         return s

        for key, value in hash_map.items():
            command = command.replace(key, value)
        return command
