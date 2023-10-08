# Source : https://leetcode.com/problems/binary-search/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a 
# function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# Example 1:
# 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# 
# Example 2:
# 
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
# 
# Constraints:
# 
# 	1 <= nums.length <= 10^4
# 	-10^4 < nums[i], target < 10^4
# 	All the integers in nums are unique.
# 	nums is sorted in ascending order.
#####################################################################################################

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n - 1
        while l<=r:
            p = (l + r) / 2
            if nums[p] > target:
                r = p - 1
            elif nums[p] < target:
                l = p + 1
            else:
                return p
        return -1
