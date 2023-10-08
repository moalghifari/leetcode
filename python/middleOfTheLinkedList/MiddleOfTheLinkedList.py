# Source : https://leetcode.com/problems/middle-of-the-linked-list/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given the head of a singly linked list, return the middle node of the linked list.
# 
# If there are two middle nodes, return the second middle node.
# 
# Example 1:
# 
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# 
# Example 2:
# 
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
# 
# Constraints:
# 
# 	The number of nodes in the list is in the range [1, 100].
# 	1 <= Node.val <= 100
#####################################################################################################

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        global mid_list
        new_head, pos, mid_pos = rec(head, 1, 0)
        return new_head
        
def rec(head, pos, mid_pos):
    global mid_list
    if not head.next:
        if pos % 2 == 0:
            mid_pos = (pos / 2) + 1
        else:
            mid_pos = (pos + 1) / 2
        return head, pos, mid_pos
    
    next_list, pos, mid_pos = rec(head.next, pos+1, mid_pos)
    if pos == mid_pos:
        mid_list = next_list
    if pos <= mid_pos:
        return next_list, pos, mid_pos
    return head, pos-1, mid_pos
