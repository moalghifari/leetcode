# Source : https://leetcode.com/problems/unique-paths/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., 
# grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The 
# robot can only move either down or right at any point in time.
# 
# Given the two integers m and n, return the number of possible unique paths that the robot can take 
# to reach the bottom-right corner.
# 
# The test cases are generated so that the answer will be less than or equal to 2 * 10^9.
# 
# Example 1:
# 
# Input: m = 3, n = 7
# Output: 28
# 
# Example 2:
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
# 
# Constraints:
# 
# 	1 <= m, n <= 100
#####################################################################################################

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        unique_paths = [[0 for _ in range(0,n)] for _ in range(0,m)]
        unique_paths[0][0] = 1
        for i in range(0,m):
            for j in range(0,n):
                if unique_paths[i][j]:
                    continue
                up = unique_paths[i-1][j] if i > 0 else 0
                left = unique_paths[i][j-1] if j > 0 else 0
                unique_paths[i][j] = up + left
        return unique_paths[m-1][n-1]
