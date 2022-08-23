'''
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        if bills[0] > 5:
            return False
        
        curr = 0
        
        count_5 = 0
        count_10 = 0
        count_20 = 0
        
        for bill in bills:
            if bill == 5:
                count_5 += 1  
                
            elif bill == 10:
                if count_5 == 0:
                    return False
                else:
                    count_5 -= 1
                    count_10 += 1
            elif bill == 20:
                if count_5 == 0:
                    return False
                elif count_10 == 0:
                    if count_5 < 3:
                        return False
                    else:
                        count_5 -= 3
                else:
                    count_10 -= 1
                    count_5 -= 1
        return True
        
