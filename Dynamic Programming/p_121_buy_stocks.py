'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## naive Solution
#         profit = 0
#         day = 0
#         for i in range(len(prices)-1):
#             for j in range(i+1,len(prices)):
#                 diff = prices[j] - prices[i]
#                 if diff >= profit:
#                     profit = diff
#                     day = j
                            
#         return profit
        
        ## O(n) solution
        left = 0
        right = 1
        
        profit = 0
        
        while right < len(prices):
            curr_diff = prices[right] - prices[left]
            
            if prices[left] < prices[right]:
                profit = max(curr_diff, profit)
            else:
                left = right
            right +=1
        return profit
