# Source : https://leetcode.com/problems/backspace-string-compare/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given two strings s and t, return true if they are equal when both are typed into empty text 
# editors. '#' means a backspace character.
# 
# Note that after backspacing an empty text, the text will continue empty.
# 
# Example 1:
# 
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# 
# Example 2:
# 
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# 
# Example 3:
# 
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
# 
# Constraints:
# 
# 	1 <= s.length, t.length <= 200
# 	s and t only contain lowercase letters and '#' characters.
# 
# Follow up: Can you solve it in O(n) time and O(1) space?
#####################################################################################################

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_s, stack_t = [], []
        for ch in s:
            if ch == '#' and stack_s:
                stack_s.pop()
            elif ch != '#':
                stack_s.append(ch)
        for ch in t:
            if ch == '#' and stack_t:
                stack_t.pop()
            elif ch != '#':
                stack_t.append(ch)
        n_s = len(stack_s)
        n_t = len(stack_t)
        if n_s != n_t:
            return False
        for i in range(0, n_s):
            if stack_s[i] != stack_t[i]:
                return False
        return True
        
