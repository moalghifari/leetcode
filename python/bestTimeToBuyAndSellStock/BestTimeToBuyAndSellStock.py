# Source : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# You are given an array prices where prices[i] is the price of a given stock on the i^th day.
# 
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different 
# day in the future to sell that stock.
# 
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, 
# return 0.
# 
# Example 1:
# 
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# 
# Example 2:
# 
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
# 
# Constraints:
# 
# 	1 <= prices.length <= 10^5
# 	0 <= prices[i] <= 10^4
#####################################################################################################

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        ptr_left = 0
        ptr_right = 1
        while ptr_right < len(prices):
            cur_profit = prices[ptr_right] - prices[ptr_left]
            if cur_profit >= 0:
                max_profit = max(cur_profit, max_profit)
            else:
                ptr_left = ptr_right
            ptr_right += 1
        return max_profit
