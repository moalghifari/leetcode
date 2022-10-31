// Source : https://leetcode.com/problems/jump-game/
// Author : Mochamad Alghifari
// Date   : 2022-10-31

/***************************************************************************************************** 
 *
 * You are given an integer array nums. You are initially positioned at the array's first index, and 
 * each element in the array represents your maximum jump length at that position.
 * 
 * Return true if you can reach the last index, or false otherwise.
 * 
 * Example 1:
 * 
 * Input: nums = [2,3,1,1,4]
 * Output: true
 * Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
 * 
 * Example 2:
 * 
 * Input: nums = [3,2,1,0,4]
 * Output: false
 * Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which 
 * makes it impossible to reach the last index.
 * 
 * Constraints:
 * 
 * 	1 <= nums.length <= 10^4
 * 	0 <= nums[i] <= 10^5
 ******************************************************************************************************/

class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        int jump = nums[0];
        if (n == 1) return true;
        if (jump == 0) return false;
        for (int i = 0; i < n - 1; i++) {
            jump = Math.max(jump - 1, nums[i]);
            if (jump == 0) return false;
        }
        return true;
    }
}
