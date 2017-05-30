'''
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    nums.sort()
    i = 0
    while i < len(nums):
        if i == len(nums) - 1:
            return nums[i]
        if nums[i] == nums[i + 1] == nums[i + 2]:
            i += 3
        else:
            return nums[i]


nums = [ 2,3,2,2]
print singleNumber(nums)
