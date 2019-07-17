'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''

#DP:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = prices
        l = len(prices)
        
        buy = [0]*(l+2)
        sell = [0]*(l+1)
        
        for i in range(l-1, -1, -1):
            sell[i] = max(sell[i+1], buy[i+2] + a[i])
            buy[i] = max(buy[i+1], sell[i+1] - a[i])
        
        return buy[0]
