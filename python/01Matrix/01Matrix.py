# Source : https://leetcode.com/problems/01-matrix/
# Author : Mochamad Alghifari
# Date   : 2022-10-08

##################################################################################################### 
#
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# 
# The distance between two adjacent cells is 1.
# 
# Example 1:
# 
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# 
# Example 2:
# 
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
# 
# Constraints:
# 
# 	m == mat.length
# 	n == mat[i].length
# 	1 <= m, n <= 10^4
# 	1 <= m * n <= 10^4
# 	mat[i][j] is either 0 or 1.
# 	There is at least one 0 in mat.
#####################################################################################################

import math
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = []
        m = len(mat)
        n = len(mat[0])
        visited = [[0 for _ in range(0, n)] for _ in range(0, m)]
        for i in range(0, m):
            for j in range(0, n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = 1
        
        while queue:
            x, y = queue.pop(0)
            for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if a >= 0 and a < m and b >= 0 and b < n and not visited[a][b]:
                    mat[a][b] = mat[x][y] + 1
                    visited[a][b] = 1
                    queue.append((a,b))
        return mat
