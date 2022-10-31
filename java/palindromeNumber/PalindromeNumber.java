// Source : https://leetcode.com/problems/palindrome-number/
// Author : Mochamad Alghifari
// Date   : 2022-10-31

/***************************************************************************************************** 
 *
 * Given an integer x, return true if x is a palindrome, and false otherwise.
 * 
 * Example 1:
 * 
 * Input: x = 121
 * Output: true
 * Explanation: 121 reads as 121 from left to right and from right to left.
 * 
 * Example 2:
 * 
 * Input: x = -121
 * Output: false
 * Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it 
 * is not a palindrome.
 * 
 * Example 3:
 * 
 * Input: x = 10
 * Output: false
 * Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 * 
 * Constraints:
 * 
 * 	-2^31 <= x <= 2^31 - 1
 * 
 * Follow up: Could you solve it without converting the integer to a string?
 ******************************************************************************************************/

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0 || (x != 0 && x % 10 == 0)) return false;
        int reverseNumber = 0;
        while (x > reverseNumber) {
            int remainder = x % 10;
            reverseNumber = (reverseNumber * 10) + remainder;
            x = x / 10;
        }
        return (x == reverseNumber || x == reverseNumber / 10);
    }
}
