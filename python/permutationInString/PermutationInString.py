# Source : https://leetcode.com/problems/permutation-in-string/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# 
# In other words, return true if one of s1's permutations is the substring of s2.
# 
# Example 1:
# 
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# Example 2:
# 
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# 
# Constraints:
# 
# 	1 <= s1.length, s2.length <= 10^4
# 	s1 and s2 consist of lowercase English letters.
#####################################################################################################

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_counter = {}
        for s in s1:
            if s not in s1_counter:
                s1_counter[s] = 0
            s1_counter[s] += 1
        
        n_s1 = len(s1)
        n_s2 = len(s2)
        for i in range(0, n_s2):
            if s2[i] in s1_counter:
                s1_counter[s2[i]] -= 1
            if i >= n_s1 and s2[i - n_s1] in s1_counter:
                s1_counter[s2[i - n_s1]] += 1
            
            if all(s1_counter[c] == 0 for c in s1_counter):
                return True
        return False:
