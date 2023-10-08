# Source : https://leetcode.com/problems/isomorphic-strings/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while preserving the order 
# of characters. No two characters may map to the same character, but a character may map to itself.
# 
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
# Input: s = "paper", t = "title"
# Output: true
# 
# Constraints:
# 
# 	1 <= s.length <= 5 * 10^4
# 	t.length == s.length
# 	s and t consist of any valid ascii character.
#####################################################################################################

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_s = map_of_string(s)
        map_t = map_of_string(t)
        if map_s == map_t:
            return True
        return False
        
        
def map_of_string(str):
    map_str = []
    dict_str = {}
    for idx, ltr in enumerate(str):
        if ltr not in dict_str:
            dict_str[ltr] = idx
        map_str.append(dict_str[ltr])
        
    return map_str
