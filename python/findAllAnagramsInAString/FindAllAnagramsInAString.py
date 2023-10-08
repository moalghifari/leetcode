# Source : https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may 
# return the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.
# 
# Example 1:
# 
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# Example 2:
# 
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# Constraints:
# 
# 	1 <= s.length, p.length <= 3 * 10^4
# 	s and p consist of lowercase English letters.
#####################################################################################################

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n_p = len(p)
        n_s = len(s)
        ans = []
        if n_p > n_s:
            return ans
        phash = {}
        shash = {}
        left = 0
        right = 0
        while right < n_p:
            if p[right] not in phash:
                phash[p[right]] = 0
            if s[right] not in shash:
                shash[s[right]] = 0
            phash[p[right]] += 1
            shash[s[right]] += 1
            right += 1
        right -= 1
        while right < n_s:
            if phash == shash:
                ans.append(left)
            right += 1
            if right != n_s:
                shash[s[left]] -= 1
                if shash[s[left]] == 0:
                    del shash[s[left]]
                if s[right] not in shash:
                    shash[s[right]] = 0
                shash[s[right]] += 1
            left += 1
        return ans
