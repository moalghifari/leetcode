# Source : https://leetcode.com/problems/number-of-islands/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return 
# the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or 
# vertically. You may assume all four edges of the grid are all surrounded by water.
# 
# Example 1:
# 
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# 
# Example 2:
# 
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
# 
# Constraints:
# 
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 300
# 	grid[i][j] is '0' or '1'.
#####################################################################################################

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] == "0" or visited[i][j] == 1:
                return
            visited[i][j] = 1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        num_of_islands = 0
        for x in range(0, m):
            for y in range(0, n):
                if grid[x][y] == "1" and visited[x][y] == 0:
                    dfs(x, y)
                    num_of_islands += 1
        return num_of_islands
