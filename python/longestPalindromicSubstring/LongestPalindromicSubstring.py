# Source : https://leetcode.com/problems/longest-palindromic-substring/
# Author : Mochamad Alghifari
# Date   : 2023-10-04

##################################################################################################### 
#
# Given a string s, return the longest palindromic substring in s.
# 
# Example 1:
# 
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# Example 2:
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# Constraints:
# 
# 	1 <= s.length <= 1000
# 	s consist of only digits and English letters.
#####################################################################################################

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        for i in range(0, len(s)):
            len_single = longestPalindromeString(s, i, i)
            len_double = longestPalindromeString(s, i, i+1)
            len_max = max(len_single, len_double)
            if len_max > end - start:
                start = i - (len_max - 1)//2
                end = i + len_max//2
        return s[start:end+1]
        
def longestPalindromeString(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1
