# Source : https://leetcode.com/problems/decode-string/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given an encoded string, return its decoded string.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is 
# being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# 
# You may assume that the input string is always valid; there are no extra white spaces, square 
# brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain 
# any digits and that digits are only for those repeat numbers, k. For example, there will not be 
# input like 3a or 2[4].
# 
# The test cases are generated so that the length of the output will never exceed 10^5.
# 
# Example 1:
# 
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# 
# Example 2:
# 
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# 
# Example 3:
# 
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# 
# Constraints:
# 
# 	1 <= s.length <= 30
# 	s consists of lowercase English letters, digits, and square brackets '[]'.
# 	s is guaranteed to be a valid input.
# 	All the integers in s are in the range [1, 300].
#####################################################################################################

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i, n = 0, len(s)
        while i < n:
            if s[i] == ']':
                encoded_string = ''
                ch = stack.pop()
                while ch != '[':
                    encoded_string = ch + encoded_string
                    ch = stack.pop()
                dig = stack.pop()
                num = dig
                while stack and len(stack[-1]) == 1 and ord(stack[-1]) >= 48 and ord(stack[-1]) <= 57:
                    dig = stack.pop()
                    num = dig + num
                for j in range(0, int(num)):
                    stack.append(encoded_string)
            else:
                stack.append(s[i])
            i += 1
        return ''.join(stack)
