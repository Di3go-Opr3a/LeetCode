# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
x = 1001

x = str(x)
if x == x[::-1]:
    return True
else:
    return False