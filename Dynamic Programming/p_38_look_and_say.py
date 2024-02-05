class Solution:
    def countAndSay(self, n: int) -> str:

        string_table = n * ['1']

        for i in range(1, n): 
            str_temp = ''
            j = 0
            while j < len(string_table[i-1]):
                count = 1
                while j+1 < len(string_table[i-1]) and string_table[i-1][j] == string_table[i-1][j+1]:
                    count += 1
                    j += 1

                str_temp += str(count) + string_table[i-1][j]
                j += 1
            
            string_table[i] = str_temp

        return string_table[n-1]


        
