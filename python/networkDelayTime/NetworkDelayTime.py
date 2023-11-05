# Source : https://leetcode.com/problems/network-delay-time/
# Author : Mochamad Alghifari
# Date   : 2023-11-05

##################################################################################################### 
#
# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel 
# times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target 
# node, and wi is the time it takes for a signal to travel from source to target.
# 
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to 
# receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
# 
# Example 1:
# 
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# 
# Example 2:
# 
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# 
# Example 3:
# 
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
# 
# Constraints:
# 
# 	1 <= k <= n <= 100
# 	1 <= times.length <= 6000
# 	times[i].length == 3
# 	1 <= ui, vi <= n
# 	ui != vi
# 	0 <= wi <= 100
# 	All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
#####################################################################################################


import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = [[-1 for i in range(0,n+1)] for i in range(0,n+1)]
        for time in times:
            graph[time[0]][time[1]] = time[2]
        
        visited = [-1] * (n+1)
        heap = []
        heapq.heappush(heap, (0, k))
        while len(heap) > 0:
            time, node = heapq.heappop(heap)
            if visited[node] == -1:
                visited[node] = time
            else:
                continue

            for i in range(1, n+1):
                if graph[node][i] != -1:
                    heapq.heappush(heap, (time + graph[node][i], i))
        
        max_time = -1
        for i in range(1, n+1):
            if visited[i] == -1:
                return -1
            if visited[i] > max_time:
                max_time = visited[i]

        return max_time
