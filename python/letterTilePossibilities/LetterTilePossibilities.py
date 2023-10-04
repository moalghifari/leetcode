# Source : https://leetcode.com/problems/letter-tile-possibilities/
# Author : Mochamad Alghifari
# Date   : 2023-10-04

##################################################################################################### 
#
# You have n  tiles, where each tile has one letter tiles[i] printed on it.
# 
# Return the number of possible non-empty sequences of letters you can make using the letters printed 
# on those tiles.
# 
# Example 1:
# 
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# 
# Example 2:
# 
# Input: tiles = "AAABBC"
# Output: 188
# 
# Example 3:
# 
# Input: tiles = "V"
# Output: 1
# 
# Constraints:
# 
# 	1 <= tiles.length <= 7
# 	tiles consists of uppercase English letters.
#####################################################################################################

import itertools
import math

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        iter = tiles
        sum = 0
        for i in range(1, len(iter) + 1):
            combs = itertools.combinations(iter, i)
            # SORT COMBINATIONS
            list_of_combs = []
            for com in combs:
                com = sorted(com)
                list_of_combs.append(com)
            list_of_combs = sorted(list_of_combs)

            prev_com = ()
            for com in list_of_combs:
                # SKIP SAME COMBINATION
                if com == prev_com:
                    continue

                # GET EACH count_letters OF SAME LETTER
                count_letters = []
                count_letter = 0
                prev_char = ''
                for char in com:
                    if char == prev_char:
                        count_letter += 1
                    else:
                        if count_letter != 0:
                            count_letters.append(count_letter)
                        count_letter = 1
                    prev_char = char
                count_letters.append(count_letter)

                # CALCULATE TOTAL FACTORIAL OF EACH count_letter
                div = 1
                for j in count_letters:
                    div *= math.factorial(j)

                # CALCULATE PERMUTATION
                n_permutation = math.factorial(len(com)) / div

                # NEXT COMBINATION
                prev_com = com
                sum += n_permutation

        return sum
