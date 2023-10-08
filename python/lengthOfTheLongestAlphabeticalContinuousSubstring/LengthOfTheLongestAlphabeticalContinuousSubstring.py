# Source : https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In 
# other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".
# 
# 	For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
# 
# Given a string s consisting of lowercase letters only, return the length of the longest 
# alphabetical continuous substring.
# 
# Example 1:
# 
# Input: s = "abacaba"
# Output: 2
# Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
# "ab" is the longest continuous substring.
# 
# Example 2:
# 
# Input: s = "abcde"
# Output: 5
# Explanation: "abcde" is the longest continuous substring.
# 
# Constraints:
# 
# 	1 <= s.length <= 10^5
# 	s consists of only English lowercase letters.
#####################################################################################################

class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 1:
            return n
        max_count = 1
        i = 1
        count = 1
        prev_char = ord(s[0])
        while i < n:
            cur_char = ord(s[i])
            if cur_char - prev_char == 1:
                count += 1
                max_count = max(count, max_count)
            else:
                count = 1
            prev_char = cur_char
            i += 1
        return max_count
