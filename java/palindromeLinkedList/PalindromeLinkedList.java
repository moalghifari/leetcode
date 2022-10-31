// Source : https://leetcode.com/problems/palindrome-linked-list/
// Author : Mochamad Alghifari
// Date   : 2022-10-31

/***************************************************************************************************** 
 *
 * Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
 * 
 * Example 1:
 * 
 * Input: head = [1,2,2,1]
 * Output: true
 * 
 * Example 2:
 * 
 * Input: head = [1,2]
 * Output: false
 * 
 * Constraints:
 * 
 * 	The number of nodes in the list is in the range [1, 10^5].
 * 	0 <= Node.val <= 9
 * 
 * Follow up: Could you do it in O(n) time and O(1) space?
 ******************************************************************************************************/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    ListNode start;
    
    public boolean isPalindrome(ListNode head) {
        start = head;
        return compareVal(head);
    }
    
    public boolean compareVal(ListNode node) {
        if (node == null) return true;
        boolean ans = compareVal(node.next);
        boolean isEqual = node.val == start.val;
        start = start.next;
        return ans && isEqual;
    }
}
