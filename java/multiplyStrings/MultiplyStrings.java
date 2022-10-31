// Source : https://leetcode.com/problems/multiply-strings/
// Author : Mochamad Alghifari
// Date   : 2022-10-31

/***************************************************************************************************** 
 *
 * Given two non-negative integers num1 and num2 represented as strings, return the product of num1 
 * and num2, also represented as a string.
 * 
 * Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
 * 
 * Example 1:
 * Input: num1 = "2", num2 = "3"
 * Output: "6"
 * Example 2:
 * Input: num1 = "123", num2 = "456"
 * Output: "56088"
 * 
 * Constraints:
 * 
 * 	1 <= num1.length, num2.length <= 200
 * 	num1 and num2 consist of digits only.
 * 	Both num1 and num2 do not contain any leading zero, except the number 0 itself.
 ******************************************************************************************************/

class Solution {
    public String multiply(String num1, String num2) {
        int m = num1.length();
        int n = num2.length();
        int[] position = new int[m + n];
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int product = (num1.charAt(i) - '0') * (num2.charAt(j) - '0');
                int pos1 = i + j;
                int pos2 = pos1 + 1;
                int sum = product + position[pos2];
                position[pos1] += sum / 10;
                position[pos2] = sum % 10;
            }
        }
        StringBuilder result = new StringBuilder();
        for (int num : position) {
            if (num != 0 || result.length() != 0) {
                result.append(num);
            }
        }
        return result.length() == 0 ? "0" : result.toString(); 
    }
}
