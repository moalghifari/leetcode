# Source : https://leetcode.com/problems/bulls-and-cows/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# You are playing the Bulls and Cows game with your friend.
# 
# You write down a secret number and ask your friend to guess what the number is. When your friend 
# makes a guess, you provide a hint with the following info:
# 
# 	The number of "bulls", which are digits in the guess that are in the correct position.
# 	The number of "cows", which are digits in the guess that are in your secret number but are 
# located in the wrong position. Specifically, the non-bull digits in the guess that could be 
# rearranged such that they become bulls.
# 
# Given the secret number secret and your friend's guess guess, return the hint for your friend's 
# guess.
# 
# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. 
# Note that both secret and guess may contain duplicate digits.
# 
# Example 1:
# 
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"
# 
# Example 2:
# 
# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only 
# be rearranged to allow one 1 to be a bull.
# 
# Constraints:
# 
# 	1 <= secret.length, guess.length <= 1000
# 	secret.length == guess.length
# 	secret and guess consist of digits only.
#####################################################################################################

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n = len(secret)
        bulls, cows, counter_secret, counter_guess = 0, 0, {}, {}
        for i in range(0, n):
            if secret[i] not in counter_secret:
                counter_secret[secret[i]] = 0
            counter_secret[secret[i]] += 1
            if guess[i] not in counter_guess:
                counter_guess[guess[i]] = 0
            counter_guess[guess[i]] += 1
            if secret[i] == guess[i]:
                bulls += 1
        for digit in counter_secret:
            if digit in counter_guess:
                cows += min(counter_secret[digit], counter_guess[digit])
        cows = cows - bulls
        return "{}A{}B".format(bulls, cows)
