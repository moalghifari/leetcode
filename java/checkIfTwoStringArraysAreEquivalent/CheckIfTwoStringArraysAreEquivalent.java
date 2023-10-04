// Source : https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
// Author : Mochamad Alghifari
// Date   : 2023-10-04

/***************************************************************************************************** 
 *
 * Given two string arrays word1 and word2, return true if the two arrays represent the same string, 
 * and false otherwise.
 * 
 * A string is represented by an array if the array elements concatenated in order forms the string.
 * 
 * Example 1:
 * 
 * Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
 * Output: true
 * Explanation:
 * word1 represents string "ab" + "c" -> "abc"
 * word2 represents string "a" + "bc" -> "abc"
 * The strings are the same, so return true.
 * 
 * Example 2:
 * 
 * Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
 * Output: false
 * 
 * Example 3:
 * 
 * Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
 * Output: true
 * 
 * Constraints:
 * 
 * 	1 <= word1.length, word2.length <= 10^3
 * 	1 <= word1[i].length, word2[i].length <= 10^3
 * 	1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
 * 	word1[i] and word2[i] consist of lowercase letters.
 ******************************************************************************************************/

class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        int ptr1 = 0, ptr2 = 0, arrPtr1 = 0, arrPtr2 = 0;
        while (arrPtr1 < word1.length && arrPtr2 < word2.length) {
            if (word1[arrPtr1].charAt(ptr1) != word2[arrPtr2].charAt(ptr2)) return false;
            if (ptr1 == word1[arrPtr1].length() - 1) {
                ptr1 = 0;
                arrPtr1++;
            } else ptr1++;
            if (ptr2 == word2[arrPtr2].length() - 1) {
                ptr2 = 0;
                arrPtr2++;
            } else ptr2++;
        }
        return arrPtr1 == word1.length && arrPtr2 == word2.length;
    }
}
