"""
Given an array of integers, every element appears twice except for one. Find that single one.
"""

def singleNumber(nums):
    nums.sort()
    for i in range(0, len(nums), 2):
        if i == len(nums) - 1:
            return nums[i]
        if nums[i] != nums[i + 1]:
            return nums[i]
