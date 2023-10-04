# Source : https://leetcode.com/problems/palindrome-linked-list/
# Author : moalghifari
# Date   : 2023-10-04

##################################################################################################### 
#
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# 
# Example 1:
# 
# Input: head = [1,2,2,1]
# Output: true
# 
# Example 2:
# 
# Input: head = [1,2]
# Output: false
# 
# Constraints:
# 
# 	The number of nodes in the list is in the range [1, 10^5].
# 	0 <= Node.val <= 9
# 
# Follow up: Could you do it in O(n) time and O(1) space?
#####################################################################################################

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        global input_head
        input_head = head
        return rec(head)
        
def rec(r_list):
    global input_head
    
    if not r_list:
        return True
    
    is_equal_so_far = rec(r_list.next)
    
    is_equal = r_list.val == input_head.val
    input_head = input_head.next
    
    return is_equal_so_far and is_equal
