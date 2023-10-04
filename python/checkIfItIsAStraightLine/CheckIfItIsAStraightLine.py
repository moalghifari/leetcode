# Source : https://leetcode.com/problems/check-if-it-is-a-straight-line/
# Author : Mochamad Alghifari
# Date   : 2023-10-04

##################################################################################################### 
#
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate 
# of a point. Check if these points make a straight line in the XY plane.
# 
# Example 1:
# 
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# 
# Example 2:
# 
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
# 
# Constraints:
# 
# 	2 <= coordinates.length <= 1000
# 	coordinates[i].length == 2
# 	-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# 	coordinates contains no duplicate point.
#####################################################################################################

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        delta_y = (coordinates[1][1] - coordinates[0][1])
        delta_x = (coordinates[1][0] - coordinates[0][0])
        if delta_x == 0:
            m_prev = 'inf'
        else:
            m_prev = delta_y / delta_x
        for i in range(2, len(coordinates)):
            delta_y = (coordinates[i][1] - coordinates[i-1][1])
            delta_x = (coordinates[i][0] - coordinates[i-1][0])
            if delta_x == 0:
                m = 'inf'
            else:
                m = delta_y / delta_x
            if m_prev != m:
                return False
            m_prev = m
        return True
