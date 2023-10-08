# Source : https://leetcode.com/problems/max-area-of-island/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are 
# surrounded by water.
# 
# The area of an island is the number of cells with a value 1 in the island.
# 
# Return the maximum area of an island in grid. If there is no island, return 0.
# 
# Example 1:
# 
# Input: grid = 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,
# 0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,
# 0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# 
# Example 2:
# 
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
# 
# Constraints:
# 
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 50
# 	grid[i][j] is either 0 or 1.
#####################################################################################################

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] == 0:
                return 0
            if visited[i][j] == 1:
                return 0
            visited[i][j] = 1
            area = grid[i][j] + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            return area
            
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(0, n)] for _ in range(0, m)]
        max_area = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] and not visited[i][j]:
                    area = dfs(i, j)
                    max_area = max(area, max_area)
        return max_area
