# Source : https://leetcode.com/problems/power-of-three/
# Author : Mochamad Alghifari
# Date   : 2023-10-04

##################################################################################################### 
#
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# 
# An integer n is a power of three, if there exists an integer x such that n == 3^x.
# 
# Example 1:
# 
# Input: n = 27
# Output: true
# Explanation: 27 = 3^3
# 
# Example 2:
# 
# Input: n = 0
# Output: false
# Explanation: There is no x where 3^x = 0.
# 
# Example 3:
# 
# Input: n = -1
# Output: false
# Explanation: There is no x where 3^x = (-1).
# 
# Constraints:
# 
# 	-2^31 <= n <= 2^31 - 1
# 
# Follow up: Could you solve it without loops/recursion?
#####################################################################################################

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        max_power_three_under_int = 1162261467
        return n > 0 and max_power_three_under_int % n == 0
