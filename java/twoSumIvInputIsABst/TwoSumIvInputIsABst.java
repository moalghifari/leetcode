// Source : https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
// Author : Mochamad Alghifari
// Date   : 2022-10-09

/***************************************************************************************************** 
 *
 * Given the root of a Binary Search Tree and a target number k, return true if there exist two 
 * elements in the BST such that their sum is equal to the given target.
 * 
 * Example 1:
 * 
 * Input: root = [5,3,6,2,4,null,7], k = 9
 * Output: true
 * 
 * Example 2:
 * 
 * Input: root = [5,3,6,2,4,null,7], k = 28
 * Output: false
 * 
 * Constraints:
 * 
 * 	The number of nodes in the tree is in the range [1, 10^4].
 * 	-10^4 <= Node.val <= 10^4
 * 	root is guaranteed to be a valid binary search tree.
 * 	-10^5 <= k <= 10^5
 ******************************************************************************************************/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean findTarget(TreeNode root, int k) {
        HashSet<Integer> set = new HashSet<>();
        return dfs(root, set, k);
    }
    
    private boolean dfs(TreeNode node, HashSet<Integer> set, int target) {
        if (node == null) return false;
        if (set.contains(target - node.val)) return true;
        set.add(node.val);
        return dfs(node.left, set, target) || dfs(node.right, set, target);
    }
}
