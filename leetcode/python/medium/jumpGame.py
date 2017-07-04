"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    length = len(nums)
    if length <= 1:
        return True
    else:
        index = length - 2
        while index > -1:
            if index + nums[index] >= length - 1:
                return canJump(nums[:index + 1])
            index -= 1
        if index == -1:
            return False

def iterativeCanJump(nums):
    length = len(nums)
    while length > 0:
        if len(nums) < 2:
            return True
        index = len(nums) - 2
        while index > -1:
            if index + nums[index] >= length - 1:
                nums = nums[:index + 1]
                length = len(nums)
                break
            index -= 1
        if index == -1:
            return False
    return True

# Solution from site
def efficientCanJump(nums):
    index = 0
    reachable = 0
    while index <= len(nums) -1:
        if index > reachable:
            return False
        reachable = max(reachable, index + nums[index])
        index += 1
    return True

nums = [0]
print efficientCanJump(nums)
