# Source : https://leetcode.com/problems/count-days-spent-together/
# Author : Mochamad Alghifari
# Date   : 2023-10-08

##################################################################################################### 
#
# Alice and Bob are traveling to Rome for separate business meetings.
# 
# You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city 
# from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates 
# arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", 
# corresponding to the month and day of the date.
# 
# Return the total number of days that Alice and Bob are in Rome together.
# 
# You can assume that all dates occur in the same calendar year, which is not a leap year. Note that 
# the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 
# 31].
# 
# Example 1:
# 
# Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
# Output: 3
# Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 
# to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
# 
# Example 2:
# 
# Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
# Output: 0
# Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.
# 
# Constraints:
# 
# 	All dates are provided in the format "MM-DD".
# 	Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
# 	The given dates are valid dates of a non-leap year.
#####################################################################################################

class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        acc_month = [0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(2, 12):
            acc_month[i] = acc_month[i - 1] + month[i - 1]
        
        arriveAlice = arriveAlice.split('-')
        leaveAlice = leaveAlice.split('-')
        arriveBob = arriveBob.split('-')
        leaveBob = leaveBob.split('-')
        
        arriveAliceDay = acc_month[int(arriveAlice[0]) - 1] + int(arriveAlice[1])
        leaveAliceDay = acc_month[int(leaveAlice[0]) - 1] + int(leaveAlice[1])
        arriveBobDay = acc_month[int(arriveBob[0]) - 1] + int(arriveBob[1])
        leaveBobDay = acc_month[int(leaveBob[0]) - 1] + int(leaveBob[1])
        
        print(arriveAliceDay, leaveAliceDay, arriveBobDay, leaveBobDay)
        
        if arriveAliceDay < arriveBobDay:
            if leaveAliceDay < leaveBobDay:
                if leaveAliceDay - arriveBobDay >= 0:
                    return leaveAliceDay - arriveBobDay + 1
                else:
                    return 0
            else:
                return leaveBobDay - arriveBobDay + 1
        else:
            if leaveBobDay < leaveAliceDay:
                if leaveBobDay - arriveAliceDay >= 0:
                    return leaveBobDay - arriveAliceDay + 1
                else:
                    return 0 
            else:
                return leaveAliceDay - arriveAliceDay + 1
