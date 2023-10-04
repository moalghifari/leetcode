# Source : https://leetcode.com/problems/rotate-image/
# Author : Mochamad Alghifari
# Date   : 2023-10-04

##################################################################################################### 
#
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# 
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.
# 
# Example 1:
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# 
# Example 2:
# 
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# 
# Constraints:
# 
# 	n == matrix.length == matrix[i].length
# 	1 <= n <= 20
# 	-1000 <= matrix[i][j] <= 1000
#####################################################################################################

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        base = 0
        while n >= 2:
            for i in range(base, n-1):
                point = (base, i)
                rotate_points(matrix, point, point)
            n -= 1
            base += 1
                
def rotate_points(matrix, orig, point):
    rotated = rotate_point(point, len(matrix))
    if orig != rotated:
        rotate_points(matrix, orig, rotated)
    
    if orig == point:
        return 

    swap(matrix, point, rotated)


def rotate_point(point, N):
    return (point[1], N - point[0] - 1)

def swap(matrix, p1, p2):
    temp = matrix[p2[0]][p2[1]]
    matrix[p2[0]][p2[1]] = matrix[p1[0]][p1[1]]
    matrix[p1[0]][p1[1]] = temp
    
