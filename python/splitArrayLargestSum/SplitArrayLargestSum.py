# Source : https://leetcode.com/problems/split-array-largest-sum
# Author : Mochamad Alghifari
# Date   : 2023-11-08

##################################################################################################### 
#
# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the 
# largest sum of any subarray is minimized.
# 
# Return the minimized largest sum of the split.
# 
# A subarray is a contiguous part of the array.
# 
# Example 1:
# 
# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays 
# is only 18.
# 
# Example 2:
# 
# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays 
# is only 9.
# 
# Constraints:
# 
# 	1 <= nums.length <= 1000
# 	0 <= nums[i] <= 10^6
# 	1 <= k <= min(50, nums.length)
#####################################################################################################

class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def isPossible(threshold):
            curTotal = 0
            cnt = 1
            for num in nums:
                if curTotal+num <= threshold:
                    curTotal += num
                else:
                    cnt += 1
                    curTotal = num
            if cnt > k:
                return False
            return True

        left = max(nums)
        right = sum(nums)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if isPossible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
