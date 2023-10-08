# Source : https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# You are given a 0-indexed integer array players, where players[i] represents the ability of the 
# i^th player. You are also given a 0-indexed integer array trainers, where trainers[j] represents 
# the training capacity of the j^th trainer.
# 
# The i^th player can match with the j^th trainer if the player's ability is less than or equal to 
# the trainer's training capacity. Additionally, the i^th player can be matched with at most one 
# trainer, and the j^th trainer can be matched with at most one player.
# 
# Return the maximum number of matchings between players and trainers that satisfy these conditions.
# 
# Example 1:
# 
# Input: players = [4,7,9], trainers = [8,2,5,8]
# Output: 2
# Explanation:
# One of the ways we can form two matchings is as follows:
# - players[0] can be matched with trainers[0] since 4 <= 8.
# - players[1] can be matched with trainers[3] since 7 <= 8.
# It can be proven that 2 is the maximum number of matchings that can be formed.
# 
# Example 2:
# 
# Input: players = [1,1,1], trainers = [10]
# Output: 1
# Explanation:
# The trainer can be matched with any of the 3 players.
# Each player can only be matched with one trainer, so the maximum answer is 1.
# 
# Constraints:
# 
# 	1 <= players.length, trainers.length <= 10^5
# 	1 <= players[i], trainers[j] <= 10^9
#####################################################################################################

class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        pl = 0
        tr = 0
        count = 0
        n_pl = len(players)
        n_tr = len(trainers)
        while tr < n_tr and pl < n_pl:
            if trainers[tr] >= players[pl]:
                count += 1
                tr += 1
                pl += 1
                continue
            tr += 1
        return count
