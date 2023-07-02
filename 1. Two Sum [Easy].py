# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
nums = [2,5,5,11] 
target = 10

control = False
position1 = 0
position2 = 1

while control != True:
    for x in range(position1,len(nums)):
        for y in range(position2,len(nums)):
            print(position1, position2, x, y, nums[x], nums[y])
            if target == (nums[x] + nums[y]):
                control = True
                return(x, y)
                break
        position1 += 1
        position2 += 1