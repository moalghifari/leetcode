# Source : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given the head of a linked list, remove the n^th node from the end of the list and return its head.
# 
# Example 1:
# 
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# 
# Example 2:
# 
# Input: head = [1], n = 1
# Output: []
# 
# Example 3:
# 
# Input: head = [1,2], n = 1
# Output: [1]
# 
# Constraints:
# 
# 	The number of nodes in the list is sz.
# 	1 <= sz <= 30
# 	0 <= Node.val <= 100
# 	1 <= n <= sz
# 
# Follow up: Could you do this in one pass?
#####################################################################################################

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        left = right = head
        for _ in range(n):
            right = right.next
        if not right:
            return head.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head
