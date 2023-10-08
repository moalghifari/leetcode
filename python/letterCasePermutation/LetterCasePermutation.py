# Source : https://leetcode.com/problems/letter-case-permutation/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given a string s, you can transform every letter individually to be lowercase or uppercase to 
# create another string.
# 
# Return a list of all possible strings we could create. Return the output in any order.
# 
# Example 1:
# 
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# 
# Example 2:
# 
# Input: s = "3z4"
# Output: ["3z4","3Z4"]
# 
# Constraints:
# 
# 	1 <= s.length <= 12
# 	s consists of lowercase English letters, uppercase English letters, and digits.
#####################################################################################################

class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def backtrack(i):
            if i == n:
                sol = ''
                for ch in list_of_char:
                    sol += ch
                ans.append(sol)
                return
            backtrack(i + 1)
            if list_of_char[i].isalpha():
                ord_chr = ord(list_of_char[i]) ^ (1 << 5)
                list_of_char[i] = chr(ord_chr)
                backtrack(i + 1)
            
        n = len(s)
        ans = []
        list_of_char = [ch for ch in s]
        backtrack(0)
        return ans
