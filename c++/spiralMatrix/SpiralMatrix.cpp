// Source : https://leetcode.com/problems/spiral-matrix/
// Author : Mochamad Alghifari
// Date   : 2022-10-31

/***************************************************************************************************** 
 *
 * Given an m x n matrix, return all elements of the matrix in spiral order.
 * 
 * Example 1:
 * 
 * Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * Output: [1,2,3,6,9,8,7,4,5]
 * 
 * Example 2:
 * 
 * Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
 * Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 * 
 * Constraints:
 * 
 * 	m == matrix.length
 * 	n == matrix[i].length
 * 	1 <= m, n <= 10
 * 	-100 <= matrix[i][j] <= 100
 ******************************************************************************************************/

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int left = 0, right = n - 1, top = 0, bottom = m - 1;
        vector<int> ans;
        while (left <= right && top <= bottom) {        
            for (int i = left; i <= right && top <= bottom; i++) {
                ans.push_back(matrix[top][i]);
            }
            top++;
            for (int i = top; i <= bottom && left <= right; i++) {
                ans.push_back(matrix[i][right]);
            }
            right--;
            for (int i = right; i >= left && top <= bottom; i--) {
                ans.push_back(matrix[bottom][i]);
            }
            bottom--;
            for (int i = bottom; i >= top && left <= right; i--) {
                ans.push_back(matrix[i][left]);
            }
            left++;
        }
        return ans;
    }
};
