# Source : https://leetcode.com/problems/number-of-provinces/
# Author : Mochamad Alghifari
# Date   : 2023-11-08

##################################################################################################### 
#
# There are n cities. Some of them are connected, while some are not. If city a is connected directly 
# with city b, and city b is connected directly with city c, then city a is connected indirectly with 
# city c.
# 
# A province is a group of directly or indirectly connected cities and no other cities outside of the 
# group.
# 
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the i^th city and the j^th 
# city are directly connected, and isConnected[i][j] = 0 otherwise.
# 
# Return the total number of provinces.
# 
# Example 1:
# 
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# 
# Example 2:
# 
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# 
# Constraints:
# 
# 	1 <= n <= 200
# 	n == isConnected.length
# 	n == isConnected[i].length
# 	isConnected[i][j] is 1 or 0.
# 	isConnected[i][i] == 1
# 	isConnected[i][j] == isConnected[j][i]
#####################################################################################################

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        parent = [i for i in range(0, n)]
        rank = [1 for i in range(0, n)]

        def find(node):
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(node1, node2):
            par1, par2 = find(node1), find(node2)
            if par1 == par2:
                return 0
            
            if rank[par1] >= rank[par2]:
                parent[par2] = par1
                rank[par1] += rank[par2]
            else:
                parent[par1] = par2
                rank[par2] += rank[par1]
            return 1

        ans = n
        for i in range(0, n):
            for j in range(0, n):
                if isConnected[i][j] == 1:
                    ans -= union(i, j)

        return ans
