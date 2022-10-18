// Source : https://leetcode.com/problems/count-and-say/
// Author : Mochamad Alghifari
// Date   : 2022-10-18

/***************************************************************************************************** 
 *
 * The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
 * 
 * 	countAndSay(1) = "1"
 * 	countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is 
 * then converted into a different digit string.
 * 
 * To determine how you "say" a digit string, split it into the minimal number of substrings such that 
 * each substring contains exactly one unique digit. Then for each substring, say the number of 
 * digits, then say the digit. Finally, concatenate every said digit.
 * 
 * For example, the saying and conversion for digit string "3322251":
 * 
 * Given a positive integer n, return the n^th term of the count-and-say sequence.
 * 
 * Example 1:
 * 
 * Input: n = 1
 * Output: "1"
 * Explanation: This is the base case.
 * 
 * Example 2:
 * 
 * Input: n = 4
 * Output: "1211"
 * Explanation:
 * countAndSay(1) = "1"
 * countAndSay(2) = say "1" = one 1 = "11"
 * countAndSay(3) = say "11" = two 1's = "21"
 * countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
 * 
 * Constraints:
 * 
 * 	1 <= n <= 30
 ******************************************************************************************************/

class Solution {
    public String countAndSay(int n) {
        String encoded = "1";
        for (int i = 1; i < n; i++) {
            encoded = encodeString(encoded);
        }
        return encoded;
    }
    
    private String encodeString(String str) {
        StringBuilder encoded = new StringBuilder();
        char ch = str.charAt(0);
        int count = 1;
        for (int i = 1; i < str.length(); i++) {
            if (str.charAt(i) == ch) {
                count++;
            } else {
                encoded.append(count);
                encoded.append(ch);
                ch = str.charAt(i);
                count = 1;
            }
        }
        encoded.append(count);
        encoded.append(ch);
        return encoded.toString();
    }
}
