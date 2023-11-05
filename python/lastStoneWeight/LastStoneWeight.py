# Source : https://leetcode.com/problems/last-stone-weight/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# You are given an array of integers stones where stones[i] is the weight of the i^th stone.
# 
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash 
# them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this 
# smash is:
# 
# 	If x == y, both stones are destroyed, and
# 	If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - 
# x.
# 
# At the end of the game, there is at most one stone left.
# 
# Return the weight of the last remaining stone. If there are no stones left, return 0.
# 
# Example 1:
# 
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
# 
# Example 2:
# 
# Input: stones = [1]
# Output: 1
# 
# Constraints:
# 
# 	1 <= stones.length <= 30
# 	1 <= stones[i] <= 1000
#####################################################################################################

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i, s in enumerate(stones):
            stones[i] = -s
            heapify(stones)
        while stones:
            s1 = heappop(stones)
            if not stones:
                return -s1
            s2 = heappop(stones)
            if s1 < s2:
                heappush(stones, s1 - s2)
        return 0

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = []
        for i in range(0, len(stones)):
            heap.append(-1 * stones[i])
        heapq.heapify(heap)

        while len(heap) > 1:
            first_stone = heapq.heappop(heap) * -1
            second_stone = heapq.heappop(heap) * -1
            result = first_stone - second_stone
            if result != 0:
                heapq.heappush(heap, -1 * result)
        if len(heap) == 1:
            return -1 * heap[0]
        return 0