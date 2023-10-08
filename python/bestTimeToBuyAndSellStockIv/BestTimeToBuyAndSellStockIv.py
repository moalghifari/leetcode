# Source : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# You are given an integer array prices where prices[i] is the price of a given stock on the i^th 
# day, and an integer k.
# 
# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy 
# at most k times and sell at most k times.
# 
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock 
# before you buy again).
# 
# Example 1:
# 
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# 
# Example 2:
# 
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on 
# day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# 
# Constraints:
# 
# 	1 <= k <= 100
# 	1 <= prices.length <= 1000
# 	0 <= prices[i] <= 1000
#####################################################################################################

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        if k >= n/2:
            ans = 0
            for i in range(1,n):
                if prices[i] > prices[i-1]:
                    ans += prices[i] - prices[i-1]
            return ans
        
        globalMaxProfit = [[0] * n for i in range (0, k+1)]
        for i in range(1, k+1):
            localMaxProfit = [0] * n
            for j in range(1,n):
                profit = prices[j] - prices[j-1]
                localMaxProfit[j] = max(
                    globalMaxProfit[i-1][j-1] + profit,
                    globalMaxProfit[i-1][j-1],
                    localMaxProfit[j-1] + profit
                )
                globalMaxProfit[i][j] = max(
                    globalMaxProfit[i][j-1],
                    localMaxProfit[j]
                )
        return globalMaxProfit[k][n-1]
