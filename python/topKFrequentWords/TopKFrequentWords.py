# Source : https://leetcode.com/problems/top-k-frequent-words/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given an array of strings words and an integer k, return the k most frequent strings.
# 
# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same 
# frequency by their lexicographical order.
# 
# Example 1:
# 
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# 
# Example 2:
# 
# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of 
# occurrence being 4, 3, 2 and 1 respectively.
# 
# Constraints:
# 
# 	1 <= words.length <= 500
# 	1 <= words[i].length <= 10
# 	words[i] consists of lowercase English letters.
# 	k is in the range [1, The number of unique words[i]]
# 
# Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
#####################################################################################################

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count_word = {}
        for word in words:
            if word not in count_word:
                count_word[word] = 0
            count_word[word] += 1
        sorted_count = sorted(count_word, key=lambda x: (-count_word[x], x))
        ans = sorted_count[:k]
        return ans         
