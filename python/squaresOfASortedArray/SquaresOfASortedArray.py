# Source : https://leetcode.com/problems/squares-of-a-sorted-array/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each 
# number sorted in non-decreasing order.
# 
# Example 1:
# 
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# 
# Example 2:
# 
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# 
# Constraints:
# 
# 	1 <= nums.length <= 10^4
# 	-10^4 <= nums[i] <= 10^4
# 	nums is sorted in non-decreasing order.
# 
# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) 
# solution using a different approach?
#####################################################################################################

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        l = 0
        r = len(nums) - 1
        while l <= r:
            left = abs(nums[l])
            right = abs(nums[r])
            if left > right:
                ans = [left*left] + ans
                l += 1
            else:
                ans = [right*right] + ans
                r -= 1
        return ans
