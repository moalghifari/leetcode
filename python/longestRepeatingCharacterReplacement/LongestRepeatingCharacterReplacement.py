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
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i, s in enumerate(stones):
            stones[i] = -s
            heapify(stones)
        while stones:
            s1 = heappop(stones)
            if not stones:
                return -s1
            s2 = heappop(stones)
            if s1 < s2:
                heappush(stones, s1 - s2)
        return 0
