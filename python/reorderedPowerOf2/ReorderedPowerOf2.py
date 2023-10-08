# Source : https://leetcode.com/problems/reordered-power-of-2/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# You are given an integer n. We reorder the digits in any order (including the original order) such 
# that the leading digit is not zero.
# 
# Return true if and only if we can do this so that the resulting number is a power of two.
# 
# Example 1:
# 
# Input: n = 1
# Output: true
# 
# Example 2:
# 
# Input: n = 10
# Output: false
# 
# Constraints:
# 
# 	1 <= n <= 10^9
#####################################################################################################

class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(0,31):
            if count_digits(2**i) == count_digits(n):
                return True
        return False
        
def count_digits(number):
    count = {}
    str_num = str(number)
    for i in range(0, len(str_num)):
        if str_num[i] not in count:
            count[str_num[i]] = 0
        count[str_num[i]] += 1         
    return count
