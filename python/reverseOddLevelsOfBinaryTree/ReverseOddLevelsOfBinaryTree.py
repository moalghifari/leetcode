# Source : https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.
# 
# 	For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should 
# become [18,29,11,7,4,3,1,2].
# 
# Return the root of the reversed tree.
# 
# A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.
# 
# The level of a node is the number of edges along the path between it and the root node.
# 
# Example 1:
# 
# Input: root = [2,3,5,8,13,21,34]
# Output: [2,5,3,8,13,21,34]
# Explanation: 
# The tree has only one odd level.
# The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.
# 
# Example 2:
# 
# Input: root = [7,13,11]
# Output: [7,11,13]
# Explanation: 
# The nodes at level 1 are 13, 11, which are reversed and become 11, 13.
# 
# Example 3:
# 
# Input: root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
# Output: [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
# Explanation: 
# The odd levels have non-zero values.
# The nodes at level 1 were 1, 2, and are 2, 1 after the reversal.
# The nodes at level 3 were 1, 1, 1, 1, 2, 2, 2, 2, and are 2, 2, 2, 2, 1, 1, 1, 1 after the reversal.
# 
# Constraints:
# 
# 	The number of nodes in the tree is in the range [1, 2^14].
# 	0 <= Node.val <= 10^5
# 	root is a perfect binary tree.
#####################################################################################################

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root
        queue = [root]
        queue_reversed = {}
        max_node = 1
        level = 0
        count_node = 1
        while queue:
            node = queue.pop(0)
            if level % 2 == 1:
                if level not in queue_reversed:
                    queue_reversed[level] = []
                queue_reversed[level].append(node)
            if node.left:
                queue.extend([node.left, node.right])
            if count_node == max_node:
                level += 1
                max_node = max_node * 2
                count_node = 1
            else:
                count_node += 1
        for i in range(1, level, 2):
            n = len(queue_reversed[i])
            mid = n // 2
            if n % 2 == 1:
                mid += 1
            # print(i, n, mid)
            for j in range(0, mid):
                # print(queue_reversed[i][j].val, queue_reversed[i][n - i - 1].val)
                queue_reversed[i][j].val, queue_reversed[i][n - j - 1].val = queue_reversed[i][n - j - 1].val, queue_reversed[i][j].val
                # temp = queue_reversed[i][j].val
                # queue_reversed[i][j].val = queue_reversed[i][n - i - 1].val
                # queue_reversed[i][n - i - 1].val = temp
                # print(queue_reversed[i][j].val, queue_reversed[i][n - i - 1].val)
        return root
