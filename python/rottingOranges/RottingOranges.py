# Source : https://leetcode.com/problems/rotting-oranges/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# You are given an m x n grid where each cell can have one of three values:
# 
# 	0 representing an empty cell,
# 	1 representing a fresh orange, or
# 	2 representing a rotten orange.
# 
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is 
# impossible, return -1.
# 
# Example 1:
# 
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# Example 2:
# 
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because 
# rotting only happens 4-directionally.
# 
# Example 3:
# 
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
# 
# Constraints:
# 
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 10
# 	grid[i][j] is 0, 1, or 2.
#####################################################################################################

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(0, n)] for _ in range(0, m)]
        max_level = 0
        queue = []
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        while queue:
            i, j, count = queue.pop(0)
            if visited[i][j] > 0:
                continue
            grid[i][j] = 2
            visited[i][j] = count
            for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x >= 0 and x < m and y >= 0 and y < n and visited[x][y] == 0 and grid[x][y] == 1:
                    queue.append((x, y, count + 1))
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    return -1
                max_level = max(max_level, visited[i][j])
        return max_level
