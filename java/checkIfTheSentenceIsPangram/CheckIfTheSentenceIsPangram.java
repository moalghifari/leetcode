// Source : https://leetcode.com/problems/check-if-the-sentence-is-pangram/
// Author : Mochamad Alghifari
// Date   : 2022-10-18

/***************************************************************************************************** 
 *
 * A pangram is a sentence where every letter of the English alphabet appears at least once.
 * 
 * Given a string sentence containing only lowercase English letters, return true if sentence is a 
 * pangram, or false otherwise.
 * 
 * Example 1:
 * 
 * Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
 * Output: true
 * Explanation: sentence contains at least one of every letter of the English alphabet.
 * 
 * Example 2:
 * 
 * Input: sentence = "leetcode"
 * Output: false
 * 
 * Constraints:
 * 
 * 	1 <= sentence.length <= 1000
 * 	sentence consists of lowercase English letters.
 ******************************************************************************************************/

class Solution {
    public boolean checkIfPangram(String sentence) {
        int[] isAppear = new int[26];
        int n = sentence.length();
        int counter = 26;
        for (int i = 0; i < n && counter > 0; i++) {
            if (isAppear[sentence.charAt(i) - 'a'] == 0) {
                isAppear[sentence.charAt(i) - 'a'] = 1;
                counter--;
            }
        }
        if (counter == 0) return true;
        return false;
    }
}
