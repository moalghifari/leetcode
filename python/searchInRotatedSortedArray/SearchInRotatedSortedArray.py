# Source : https://leetcode.com/problems/search-in-rotated-sorted-array/
# Author : Mochamad Alghifari
# Date   : 2023-10-04

##################################################################################################### 
#
# There is an integer array nums sorted in ascending order (with distinct values).
# 
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= 
# k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], 
# nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 
# 3 and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target, return the index of target 
# if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
# Constraints:
# 
# 	1 <= nums.length <= 5000
# 	-10^4 <= nums[i] <= 10^4
# 	All values of nums are unique.
# 	nums is an ascending array that is possibly rotated.
# 	-10^4 <= target <= 10^4
#####################################################################################################

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(arr,lo,hi):
            while lo<=hi:
                mid = (lo+hi)//2
              
                if target==arr[mid]:
                    return mid
                if target>arr[mid]:
                    lo=mid+1
                else:
                    hi=mid-1
            return -1
        
        def find_rotate_index(nums,lo,hi):
            if nums[lo]<nums[hi]:
                return 0
            while lo<=hi:
                mid = (lo+hi)//2
                if nums[mid]>nums[mid+1]:
                    return mid+1
                if nums[mid]<nums[lo]:
                    hi=mid-1
                else:
                    lo=mid+1
                
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return 0 if nums[0] == target else -1
        index =  find_rotate_index(nums,0,len(nums)-1)
      
        if nums[index]==target:
            return index
        
        if index == 0:
            ans = binary_search(nums,0,len(nums)-1)
        elif target>=nums[0]:
            ans = binary_search(nums,0,index)
        else:
            ans = binary_search(nums,index,len(nums)-1)
            
        
        
        return ans
