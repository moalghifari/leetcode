# Source : https://leetcode.com/problems/move-zeroes/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of 
# the non-zero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
# 
# Constraints:
# 
# 	1 <= nums.length <= 10^4
# 	-2^31 <= nums[i] <= 2^31 - 1
# 
# Follow up: Could you minimize the total number of operations done?
#####################################################################################################

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ptr_1 = 0
        for ptr_2 in range(0, len(nums)):
            if nums[ptr_2] != 0 and nums[ptr_1] == 0:
                nums[ptr_1], nums[ptr_2] = nums[ptr_2], nums[ptr_1]
            
            if nums[ptr_1] != 0:
                ptr_1 += 1
