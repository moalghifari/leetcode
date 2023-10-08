# Source : https://leetcode.com/problems/longest-repeating-character-replacement/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# You are given a string s and an integer k. You can choose any character of the string and change it 
# to any other uppercase English character. You can perform this operation at most k times.
# 
# Return the length of the longest substring containing the same letter you can get after performing 
# the above operations.
# 
# Example 1:
# 
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# 
# Example 2:
# 
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achive this answer too.
# 
# Constraints:
# 
# 	1 <= s.length <= 10^5
# 	s consists of only uppercase English letters.
# 	0 <= k <= s.length
#####################################################################################################

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start, max_count, max_length, n = 0, 0, 0, len(s)
        counter = {}
        for end in range(0, n):
            if s[end] not in counter:
                counter[s[end]] = 0
            counter[s[end]] += 1
            max_count = max(counter[s[end]], max_count)
            while (end - start - max_count + 1) > k:
                counter[s[start]] -= 1
                start += 1
            max_length = max(end - start + 1, max_length)
        return max_length