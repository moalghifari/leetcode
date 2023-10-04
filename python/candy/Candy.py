# Source : https://leetcode.com/problems/candy/
# Author : Mochamad Alghifari
# Date   : 2023-10-04

##################################################################################################### 
#
# There are n children standing in a line. Each child is assigned a rating value given in the integer 
# array ratings.
# 
# You are giving candies to these children subjected to the following requirements:
# 
# 	Each child must have at least one candy.
# 	Children with a higher rating get more candies than their neighbors.
# 
# Return the minimum number of candies you need to have to distribute the candies to the children.
# 
# Example 1:
# 
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies 
# respectively.
# 
# Example 2:
# 
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies 
# respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
# 
# Constraints:
# 
# 	n == ratings.length
# 	1 <= n <= 2 * 10^4
# 	0 <= ratings[i] <= 2 * 10^4
#####################################################################################################

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1 for i in range(len(ratings))]
        
        for i in range(0, len(ratings)):
            if i != 0:
                if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
                    candies[i] = candies[i-1] + 1
            
        for i in range(len(ratings)-1, -1, -1):
            if i != len(ratings)-1:
                if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                    candies[i] = max(candies[i], candies[i+1] + 1)
        
        sum = 0
        for i in range(len(candies)):
            sum += candies[i]
            
        return sum
