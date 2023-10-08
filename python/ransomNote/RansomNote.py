# Source : https://leetcode.com/problems/ransom-note/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using 
# the letters from magazine and false otherwise.
# 
# Each letter in magazine can only be used once in ransomNote.
# 
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
# 
# Constraints:
# 
# 	1 <= ransomNote.length, magazine.length <= 10^5
# 	ransomNote and magazine consist of lowercase English letters.
#####################################################################################################

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomeNote_count = count_ltr(ransomNote)
        magazine_count = count_ltr(magazine)
        for ltr in ransomeNote_count:
            if ltr not in magazine_count:
                return False
            if ransomeNote_count[ltr] > magazine_count[ltr]:
                return False
        return True
        
def count_ltr(str):
    count_dict = {}
    for ltr in str:
        if ltr not in count_dict:
            count_dict[ltr] = 0
        else:
            count_dict[ltr] += 1
    return count_dict
