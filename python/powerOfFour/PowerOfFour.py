# Source : https://leetcode.com/problems/power-of-four/
# Author : Mochamad Alghifari
# Date   : 2023-10-04

##################################################################################################### 
#
# Given an integer n, return true if it is a power of four. Otherwise, return false.
# 
# An integer n is a power of four, if there exists an integer x such that n == 4^x.
# 
# Example 1:
# Input: n = 16
# Output: true
# Example 2:
# Input: n = 5
# Output: false
# Example 3:
# Input: n = 1
# Output: true
# 
# Constraints:
# 
# 	-2^31 <= n <= 2^31 - 1
# 
# Follow up: Could you solve it without loops/recursion?
#####################################################################################################

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False

        sum = 0
        for digit in str(n):
            cur_digit = int(digit)
            sum += cur_digit

        n_prev = n / 4
        sum_n_prev = 0
        for digit in str(n_prev):
            cur_digit = int(digit)
            sum_n_prev += cur_digit
        
        power_n = (sum-1) / 3
        power_n_prev = (sum_n_prev-1) / 3
        
        power = max(power_n, power_n_prev + 1)
        predict = 4**(power)

        if n == predict:
            return True
        return False

