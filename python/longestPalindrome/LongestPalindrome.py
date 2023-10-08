# Source : https://leetcode.com/problems/longest-palindrome/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
# palindrome that can be built with those letters.
# 
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
# 
# Example 1:
# 
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# Example 2:
# 
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
# 
# Constraints:
# 
# 	1 <= s.length <= 2000
# 	s consists of lowercase and/or uppercase English letters only.
#####################################################################################################

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_letter = {}
        for l in s:
            if l not in count_letter:
                count_letter[l] = 0
            count_letter[l] += 1
        ans = 0
        for l in count_letter:
            if count_letter[l] > 1:
                if count_letter[l] % 2 == 0:
                    ans += count_letter[l]
                else:
                    ans += count_letter[l] - 1
        if ans < len(s):
            ans += 1
        return ans
