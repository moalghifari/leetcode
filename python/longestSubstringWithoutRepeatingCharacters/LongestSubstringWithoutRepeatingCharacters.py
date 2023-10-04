# Source : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Author : Mochamad Alghifari
# Date   : 2023-10-04

##################################################################################################### 
#
# Given a string s, find the length of the longest substring without repeating characters.
# 
# Example 1:
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# Example 2:
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# Example 3:
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
# Constraints:
# 
# 	0 <= s.length <= 5 * 10^4
# 	s consists of English letters, digits, symbols and spaces.
#####################################################################################################

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start_idx = 0
        finish_idx = 0
        max_length = 0
        dict_of_char = {}
        for finish_idx in range(0, len(s)):
            if s[finish_idx] in dict_of_char:
                start_idx = max(dict_of_char[s[finish_idx]], start_idx)
            max_length = max(max_length, finish_idx - start_idx + 1)
            dict_of_char[s[finish_idx]] = finish_idx + 1
        return max_length
