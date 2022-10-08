// Source : https://leetcode.com/problems/3sum-closest/
// Author : Mochamad Alghifari
// Date   : 2022-10-08

/***************************************************************************************************** 
 *
 * Given an integer array nums of length n and an integer target, find three integers in nums such 
 * that the sum is closest to target.
 * 
 * Return the sum of the three integers.
 * 
 * You may assume that each input would have exactly one solution.
 * 
 * Example 1:
 * 
 * Input: nums = [-1,2,1,-4], target = 1
 * Output: 2
 * Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 * 
 * Example 2:
 * 
 * Input: nums = [0,0,0], target = 1
 * Output: 0
 * Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 * 
 * Constraints:
 * 
 * 	3 <= nums.length <= 1000
 * 	-1000 <= nums[i] <= 1000
 * 	-10^4 <= target <= 10^4
 ******************************************************************************************************/

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int n = nums.length;
        int res = 0;
        if (n <= 3) {
            for (int i = 0; i < n; i++) {
                res += nums[i];
            }
            return res;
        }
        Arrays.sort(nums);
        res = nums[0] + nums[1] + nums[2];
        int j;
        int k;
        int sum;
        for (int i = 0; i < n; i++) {
            j = i + 1;
            k = n - 1;
            while (j < k) {
                sum = nums[i] + nums[j] + nums[k];
                if (Math.abs(target - sum) <= Math.abs(target - res)) {
                    res = sum;
                    if (res == target) return res;
                }
                if (sum > target) k--;
                else j++;
            }
        }
        return res;
    }
}
