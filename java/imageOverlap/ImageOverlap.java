// Source : https://leetcode.com/problems/image-overlap/
// Author : Mochamad Alghifari
// Date   : 2023-10-04

/***************************************************************************************************** 
 *
 * You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A 
 * binary matrix has only 0s and 1s as values.
 * 
 * We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any 
 * number of units. We then place it on top of the other image. We can then calculate the overlap by 
 * counting the number of positions that have a 1 in both images.
 * 
 * Note also that a translation does not include any kind of rotation. Any 1 bits that are translated 
 * outside of the matrix borders are erased.
 * 
 * Return the largest possible overlap.
 * 
 * Example 1:
 * 
 * Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
 * Output: 3
 * Explanation: We translate img1 to right by 1 unit and down by 1 unit.
 * 
 * The number of positions that have a 1 in both images is 3 (shown in red).
 * 
 * Example 2:
 * 
 * Input: img1 = [[1]], img2 = [[1]]
 * Output: 1
 * 
 * Example 3:
 * 
 * Input: img1 = [[0]], img2 = [[0]]
 * Output: 0
 * 
 * Constraints:
 * 
 * 	n == img1.length == img1[i].length
 * 	n == img2.length == img2[i].length
 * 	1 <= n <= 30
 * 	img1[i][j] is either 0 or 1.
 * 	img2[i][j] is either 0 or 1.
 ******************************************************************************************************/

class Solution {
    public int largestOverlap(int[][] img1, int[][] img2) {
        int N = img1.length;
        List<Integer> LA = new ArrayList<>();
        List<Integer> LB = new ArrayList<>();
        HashMap<Integer, Integer> count = new HashMap<>();
        for (int i = 0; i < N * N; ++i)
            if (img1[i / N][i % N] == 1)
                LA.add(i / N * 100 + i % N);
        for (int i = 0; i < N * N; ++i)
            if (img2[i / N][i % N] == 1)
                LB.add(i / N * 100 + i % N);
        for (int i : LA) for (int j : LB)
                count.put(i - j, count.getOrDefault(i - j, 0) + 1);
        int res = 0;
        for (int i : count.values())
            res = Math.max(res, i);
        return res;
    }
}
