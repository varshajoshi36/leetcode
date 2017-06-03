"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
    Note:

    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000
"""

def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    max_ones = 0
    while i < len(nums):
        if nums[i] == 1:
            if 0 in nums[i + 1:]:
                next_zero = nums[i + 1:].index(0)
            else:
                next_zero = len(nums[i + 1:])
            ones_len = next_zero + 1 
            if ones_len > max_ones:
                max_ones = ones_len
            i += next_zero + 1
        else:
            i += 1

    return max_ones


nums = [1] * 10000
print findMaxConsecutiveOnes(nums)
