# Source : https://leetcode.com/problems/top-k-frequent-elements/
# Author : Mochamad Alghifari
# Date   : 2023-11-05

##################################################################################################### 
#
# Given an integer array nums and an integer k, return the k most frequent elements. You may return 
# the answer in any order.
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# Constraints:
# 
# 	1 <= nums.length <= 10^5
# 	-10^4 <= nums[i] <= 10^4
# 	k is in the range [1, the number of unique elements in the array].
# 	It is guaranteed that the answer is unique.
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's 
# size.
#####################################################################################################

import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency_maps = {}
        for i in range(0, len(nums)):
            if nums[i] not in frequency_maps:
                frequency_maps[nums[i]] = 0
            frequency_maps[nums[i]] += 1
        
        heap = []
        for num in frequency_maps:
            heap.append((-1*frequency_maps[num], num))
        heapq.heapify(heap)

        ans = []
        for i in range(0, k):
            _, num = heapq.heappop(heap)
            ans.append(num)
        return ans
