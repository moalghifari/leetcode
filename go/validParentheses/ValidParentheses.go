// Source : https://leetcode.com/problems/valid-parentheses/
// Author : Mochamad Alghifari
// Date   : 2023-10-04

/***************************************************************************************************** 
 *
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the 
 * input string is valid.
 * 
 * An input string is valid if:
 * 
 * 	Open brackets must be closed by the same type of brackets.
 * 	Open brackets must be closed in the correct order.
 * 	Every close bracket has a corresponding open bracket of the same type.
 * 
 * Example 1:
 * 
 * Input: s = "()"
 * Output: true
 * 
 * Example 2:
 * 
 * Input: s = "()[]{}"
 * Output: true
 * 
 * Example 3:
 * 
 * Input: s = "(]"
 * Output: false
 * 
 * Constraints:
 * 
 * 	1 <= s.length <= 10^4
 * 	s consists of parentheses only '()[]{}'.
 ******************************************************************************************************/

package main

func isValid(s string) bool {
    if len(s) % 2 != 0 {
        return false
    }
    stack := make([]string, 0)
    for _, by := range s {
        ch := string(by)
        if ch == ")" || ch == "]" || ch == "}" {
            if len(stack) == 0 {
                return false
            } else {
                if isPaired(stack[len(stack)-1], ch) {
                    stack = stack[:len(stack) - 1]
                } else {
                    return false
                }
            }
        } else {
            stack = append(stack, ch)
        }
    }
    if len(stack) > 0 {
        return false
    }
    return true
}

func isPaired(a string, b string) bool {
    if a == "(" && b == ")" {
        return true
    }
    if a == "[" && b == "]" {
        return true
    }
    if a == "{" && b == "}" {
        return true
    }
    return false
}


