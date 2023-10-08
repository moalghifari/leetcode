# Source : https://leetcode.com/problems/reverse-linked-list/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# 
# Example 1:
# 
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# 
# Example 2:
# 
# Input: head = [1,2]
# Output: [2,1]
# 
# Example 3:
# 
# Input: head = []
# Output: []
# 
# Constraints:
# 
# 	The number of nodes in the list is the range [0, 5000].
# 	-5000 <= Node.val <= 5000
# 
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement 
# both?
#####################################################################################################

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        global dummy
        if not head:
            return head
        new_head = reverse_list(head)
        new_head.next = None
        return dummy
        
def reverse_list(head):
    global dummy
    if not head.next:
        dummy = head
        return head
    next = reverse_list(head.next)
    next.next = head
    next = next.next
    return next
