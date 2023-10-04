# Source : https://leetcode.com/problems/find-all-good-indices/
# Author : Mochamad Alghifari
# Date   : 2023-10-04

##################################################################################################### 
#
# You are given a 0-indexed integer array nums of size n and a positive integer k.
# 
# We call an index i in the range k <= i < n - k good if the following conditions are satisfied:
# 
# 	The k elements that are just before the index i are in non-increasing order.
# 	The k elements that are just after the index i are in non-decreasing order.
# 
# Return an array of all good indices sorted in increasing order.
# 
# Example 1:
# 
# Input: nums = [2,1,1,1,3,4,1], k = 2
# Output: [2,3]
# Explanation: There are two good indices in the array:
# - Index 2. The subarray [2,1] is in non-increasing order, and the subarray [1,3] is in 
# non-decreasing order.
# - Index 3. The subarray [1,1] is in non-increasing order, and the subarray [3,4] is in 
# non-decreasing order.
# Note that the index 4 is not good because [4,1] is not non-decreasing.
# 
# Example 2:
# 
# Input: nums = [2,1,1,2], k = 2
# Output: []
# Explanation: There are no good indices in this array.
# 
# Constraints:
# 
# 	n == nums.length
# 	3 <= n <= 10^5
# 	1 <= nums[i] <= 10^6
# 	1 <= k <= n / 2
#####################################################################################################

class Solution(object):
    def goodIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def is_good(center):
            count = 0
            left = center - 1
            right = center + 1
            prev_left = -1
            prev_right = -1
            while count < k:
                count += 1
                if nums[left] < prev_left:
                    return False, left, 'L'
                if nums[right] < prev_right:
                    return False, right, 'R'
                prev_left = nums[left]
                prev_right = nums[right]
                left -= 1
                right += 1
            return True, True, True
        
        n = len(nums)
        ans = []
        i = k
        while i < n - k:
            # print(ans, i)
            if len(ans) == 0 or ans[-1] != i - 1:
                res = is_good(i)
                # print(res)
                if res[0]:
                    ans.append(i)
                else:
                    if res[2] == 'L':
                        shift = k - (i - res[1])
                    else:
                        shift = res[1] - i
                    if shift > 2:
                        i += shift - 2
            else:
                left_shift = nums[i - 1] <= nums[i - 2] if i - 1 > 0 and k > 1 else True
                right_shift = nums[i + k] >= nums[i + k - 1] if i + k < n and k > 1 else True
                if left_shift and right_shift:
                    ans.append(i)
            i += 1
        return ans
